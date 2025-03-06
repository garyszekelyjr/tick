from tick.schwab.market_data import quotes


def test_quotes():
    response = quotes.quotes(["AAPL"])
    assert response.status_code == 200


def test_quote():
    response = quotes.quote("AAPL")
    assert response.status_code == 200
