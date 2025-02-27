from . import MARKET_DATA_URL


def expiration_chain(symbol: str):
    url = f"{MARKET_DATA_URL}/expirationchain"
    params = {"symbol": symbol}
    return {"url": url, "params": params}
