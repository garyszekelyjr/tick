from tick.schwab.market_data import movers


def test_movers():
    response = movers.get(movers.Symbol.NYSE)
    assert response.status_code == 200
