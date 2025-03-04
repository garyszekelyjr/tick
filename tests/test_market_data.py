import unittest

from datetime import datetime

from tick.schwab.market_data import (
    chains,
    expiration_chains,
    market_hours,
    movers,
    price_history,
    quotes,
)


class TestMarketData(unittest.TestCase):
    def test_quotes(self):
        """Test /quotes"""
        response = quotes.quotes(["AAPL"])
        self.assertEqual(response.status_code, 200)

    def test_quote(self):
        """Test /{symbolId}/quotes"""
        response = quotes.quote("AAPL")
        self.assertEqual(response.status_code, 200)

    def test_chains(self):
        """Test /chains"""
        response = chains.get("AAPL")
        self.assertEqual(response.status_code, 200)

    def test_expiration_chains(self):
        """Test /expirationchains"""
        response = expiration_chains.get("AAPL")
        self.assertEqual(response.status_code, 200)

    def test_price_history(self):
        """Test /pricehistory"""
        response = price_history.get(
            "AAPL", start_date=datetime(2025, 1, 1), end_date=datetime(2025, 1, 2)
        )
        self.assertEqual(response.status_code, 200)

    def test_movers(self):
        """Test /movers"""
        response = movers.get(movers.Symbol.NYSE)
        self.assertEqual(response.status_code, 200)

    def test_markets(self):
        """Test /markets"""
        for market in market_hours.Market:
            response = market_hours.get(market)
            self.assertEqual(response.status_code, 200)
