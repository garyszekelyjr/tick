from tick.schwab.market_data import chains


def test_chains():
    response = chains.get("AAPL")
    assert response.status_code == 200
