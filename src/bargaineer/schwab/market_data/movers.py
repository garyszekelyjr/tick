from enum import Enum

from requests import Response

from .. import client
from . import MARKET_DATA_URL


class Symbol(Enum):
    DJI = "$DJI"
    COMPX = "$COMPX"
    SPX = "$SPX"
    NYSE = "NYSE"
    NASDAQ = "NASDAQ"
    OTCBB = "OTCBB"
    INDEX_ALL = "INDEX_ALL"
    EQUITY_ALL = "EQUITY_ALL"
    OPTION_ALL = "OPTION_ALL"
    OPTION_PUT = "OPTION_PUT"
    OPTION_CALL = "OPTION_CALL"


class Sort(Enum):
    VOLUME = "VOLUME"
    TRADES = "TRADES"
    PERCENT_CHANGE_UP = "PERCENT_CHANGE_UP"
    PERCENT_CHANGE_DOWN = "PERCENT_CHANGE_DOWN"


class Frequency(Enum):
    ZERO = 0
    ONE = 1
    FIVE = 5
    TEN = 10
    THIRTY = 30
    SIXTY = 60


def get(
    symbol: Symbol, sort: Sort | None = None, frequency: Frequency | None = None
) -> Response:
    url = f"{MARKET_DATA_URL}/movers/{symbol.value}"
    params = {}
    if sort:
        params["sort"] = sort.value
    if frequency:
        params["frequency"] = frequency.value
    return client.request(url, params=params)
