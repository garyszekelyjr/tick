from enum import Enum
from typing import Dict, List

from . import MARKET_DATA_URL


class Field(Enum):
    QUOTE = "quote"
    FUNDAMENTAL = "fundamental"
    EXTENDED = "extended"
    REFERENCE = "reference"
    REGULAR = "regular"


def quotes(
    symbols: List[str],
    fields: List[Field] = [field for field in Field],
    indicative: bool = False,
) -> Dict:
    url = f"{MARKET_DATA_URL}/quotes"
    params = {
        "symbols": ",".join(symbols),
        "fields": ",".join([field.value for field in fields]),
        "indicative": str(indicative).lower(),
    }
    return {"url": url, "params": params}


def quote(
    symbol: str,
    fields: List[Field] = [field for field in Field],
) -> Dict:
    url = f"{MARKET_DATA_URL}/{symbol}/quotes"
    params = {"fields": ",".join([field.value for field in fields])}
    return {"url": url, "params": params}
