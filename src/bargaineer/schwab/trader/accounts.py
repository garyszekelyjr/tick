from . import TRADER_URL


def account_numbers() -> str:
    return f"{TRADER_URL}/accounts/accountNumbers"


def accounts() -> str:
    return f"{TRADER_URL}/accounts"


def account(account_number: str) -> str:
    return f"{TRADER_URL}/accounts/{account_number}"
