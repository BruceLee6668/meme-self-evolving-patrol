from __future__ import annotations

from typing import Any, Dict, List

from .http_client import HttpClient


GECKO_BASE = "https://api.geckoterminal.com/api/v2"


class GeckoTerminalClient:
    def __init__(self) -> None:
        self.http = HttpClient(timeout=25, retries=2, sleep_seconds=2)

    def trending_pools(self, network: str) -> List[Dict[str, Any]]:
        data = self.http.get_json(f"{GECKO_BASE}/networks/{network}/trending_pools")
        return data.get("data", []) if isinstance(data, dict) else []

    def pool_ohlcv(self, network: str, pool_address: str, timeframe: str = "hour", aggregate: int = 1, limit: int = 24) -> Dict[str, Any]:
        return self.http.get_json(
            f"{GECKO_BASE}/networks/{network}/pools/{pool_address}/ohlcv/{timeframe}",
            params={"aggregate": aggregate, "limit": limit, "currency": "usd"},
        )
