from enum import Enum

from . import MARKET_DATA_URL


class Projection(Enum):
    SYMBOL_SEARCH = "symbol-search"
    SYMBOL_REGEX = "symbol-regex"
    DESC_SEARCH = "desc-search"
    DESC_REGEX = "desc-regex"
    SEARCH = "search"
    FUNDAMENTAL = "fundamental"


def instruments(symbol: str, projection: Projection):
    url = f"{MARKET_DATA_URL}/instruments"
    params = {"symbol": symbol, "projection": projection.value}
    return {"url": url, "params": params}


def instrument(cusip_id: str):
    return f"{MARKET_DATA_URL}/instruments/{cusip_id}"
