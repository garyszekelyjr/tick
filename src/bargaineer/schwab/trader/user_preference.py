from . import TRADER_URL


def user_preference() -> str:
    return f"{TRADER_URL}/userPreference"
