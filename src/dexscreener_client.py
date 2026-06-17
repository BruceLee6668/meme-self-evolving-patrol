from __future__ import annotations

from typing import Any, Dict, List

from .http_client import HttpClient


DEX_BASE = "https://api.dexscreener.com"


class DexScreenerClient:
    def __init__(self) -> None:
        self.http = HttpClient(timeout=20, retries=2, sleep_seconds=1)

    def token_profiles_latest(self) -> List[Dict[str, Any]]:
        data = self.http.get_json(f"{DEX_BASE}/token-profiles/latest/v1")
        return data if isinstance(data, list) else []

    def token_boosts_latest(self) -> List[Dict[str, Any]]:
        data = self.http.get_json(f"{DEX_BASE}/token-boosts/latest/v1")
        return data if isinstance(data, list) else []

    def search_pairs(self, query: str) -> List[Dict[str, Any]]:
        data = self.http.get_json(f"{DEX_BASE}/latest/dex/search", params={"q": query})
        return data.get("pairs", []) if isinstance(data, dict) else []

    def token_pairs(self, chain_id: str, token_address: str) -> List[Dict[str, Any]]:
        # DEXScreener token endpoint accepts comma-separated token addresses but we keep it simple.
        data = self.http.get_json(f"{DEX_BASE}/latest/dex/tokens/{token_address}")
        pairs = data.get("pairs", []) if isinstance(data, dict) else []
        return [p for p in pairs if p.get("chainId") == chain_id]
