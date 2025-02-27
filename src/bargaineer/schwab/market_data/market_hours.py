from enum import Enum
from typing import Dict, List

from . import MARKET_DATA_URL


class Market(Enum):
    EQUITY = "equity"
    OPTION = "option"
    BOND = "bond"
    FUTURE = "future"
    FOREX = "forex"


def markets(
    markets: List[Market] = [market for market in Market],
    date: str = "",
) -> Dict:
    url = f"{MARKET_DATA_URL}/markets"
    params = {"markets": ",".join(map(lambda market: market.value, markets))}
    if date:
        params["date"] = date
    return {"url": url, "params": params}


def market(market: Market, date: str = "") -> Dict:
    url = f"{MARKET_DATA_URL}/markets/{market.value}"
    params = {}
    if date:
        params["date"] = date
    return {"url": url, "params": params}
