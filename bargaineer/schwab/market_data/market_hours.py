from enum import Enum
from typing import List

from requests import Response

from .. import client
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
) -> Response:
    url = f"{MARKET_DATA_URL}/markets"
    params = {"markets": ",".join(map(lambda market: market.value, markets))}
    if date:
        params["date"] = date
    return client.request(url, params=params)


def market(market: Market, date: str = "") -> Response:
    url = f"{MARKET_DATA_URL}/markets/{market.value}"
    params = {}
    if date:
        params["date"] = date
    return client.request(url, params=params)
