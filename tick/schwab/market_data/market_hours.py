from enum import Enum

from requests import Response

from .. import client
from . import MARKET_DATA_URL


class Market(Enum):
    EQUITY = "equity"
    OPTION = "option"
    BOND = "bond"
    FUTURE = "future"
    FOREX = "forex"


def get(*markets: Market, date: str = "") -> Response:
    if len(markets) == 0:
        markets = tuple(market for market in Market)

    url = f"{MARKET_DATA_URL}/markets"
    params = {"markets": ",".join(map(lambda market: market.value, markets))}

    if date:
        params["date"] = date

    return client.request(url, params=params)
