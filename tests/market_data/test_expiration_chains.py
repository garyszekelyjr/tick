from tick.schwab.market_data import expiration_chains


def test_expiration_chains():
    response = expiration_chains.get("AAPL")
    assert response.status_code == 200
