from __future__ import annotations

import time
from typing import Any, Dict, Optional

import requests


class HttpClient:
    """Small requests wrapper with retries and source status-friendly errors."""

    def __init__(self, timeout: int = 20, retries: int = 2, sleep_seconds: float = 1.0):
        self.timeout = timeout
        self.retries = retries
        self.sleep_seconds = sleep_seconds
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "meme-self-evolving-patrol/0.1"
        })

    def get_json(self, url: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        last_error: Optional[Exception] = None
        for attempt in range(self.retries + 1):
            try:
                resp = self.session.get(url, params=params, timeout=self.timeout)
                if resp.status_code == 429:
                    # backoff on rate limit
                    time.sleep(self.sleep_seconds * (attempt + 1) * 2)
                    continue
                resp.raise_for_status()
                return resp.json()
            except Exception as exc:  # noqa: BLE001
                last_error = exc
                if attempt < self.retries:
                    time.sleep(self.sleep_seconds * (attempt + 1))
        raise RuntimeError(f"GET failed: {url} params={params} error={last_error}")
