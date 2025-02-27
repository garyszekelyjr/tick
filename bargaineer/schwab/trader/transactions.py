from datetime import datetime
from enum import Enum
from typing import Dict

from . import TRADER_URL


class Types(Enum):
    TRADE = "TRADE"
    RECEIVE_AND_DELIVER = "RECEIVE_AND_DELIVER"
    DIVIDEND_OR_INTEREST = "DIVIDEND_OR_INTEREST"
    ACH_RECEIPT = "ACH_RECEIPT"
    ACH_DISBURSEMENT = "ACH_DISBURSEMENT"
    CASH_RECEIPT = "CASH_RECEIPT"
    CASH_DISBURSEMENT = "CASH_DISBURSEMENT"
    ELECTRONIC_FUND = "ELECTRONIC_FUND"
    WIRE_OUT = "WIRE_OUT"
    WIRE_IN = "WIRE_IN"
    JOURNAL = "JOURNAL"
    MEMORANDUM = "MEMORANDUM"
    MARGIN_CALL = "MARGIN_CALL"
    MONEY_MARKET = "MONEY_MARKET"
    SMA_ADJUSTMENT = "SMA_ADJUSTMENT"


def transactions(
    account_number: str,
    start_date: datetime,
    end_date: datetime,
    symbol: str = "",
    types: str = "",
) -> Dict:
    url = f"{TRADER_URL}/accounts/{account_number}/transactions"

    params = {
        "startDate": start_date.isoformat(),
        "endDate": end_date.isoformat(),
        "symbol": symbol,
        "types": types,
    }

    return {"url": url, "params": params}


def transaction(account_number: str, transaction_id: int) -> str:
    return f"{TRADER_URL}/accounts/{account_number}/transactions/{transaction_id}"
