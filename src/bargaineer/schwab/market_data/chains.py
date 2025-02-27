from enum import Enum
from typing import Dict

from . import MARKET_DATA_URL


class ContractType(Enum):
    CALL = "CALL"
    PUT = "PUT"
    ALL = "ALL"


def chains(
    symbol: str,
    contract_type: ContractType = ContractType.ALL,
    strike_count: int | None = None,
) -> Dict:
    url = f"{MARKET_DATA_URL}/chains"
    params = {"symbol": symbol, "contractType": contract_type.value}
    if strike_count:
        params["strikeCount"] = str(strike_count)
    return {"url": url, "params": params}
