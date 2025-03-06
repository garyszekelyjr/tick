from tick.schwab.market_data import market_hours


def test_markets():
    for market in market_hours.Market:
        response = market_hours.get(market)
        assert response.status_code == 200
