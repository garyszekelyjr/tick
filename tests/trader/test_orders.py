import unittest

from datetime import datetime

from bargaineer import TZ
from bargaineer.schwab import client


class TestOrders(unittest.TestCase):
    def setUp(self) -> None:
        response = client.request(client.ENDPOINTS["/accounts/accountNumbers"]())
        self.assertEqual(response.status_code, 200)
        self.account_numbers = response.json()

    def test_orders(self):
        """Test /orders"""
        from_entered_time = datetime(2025, 1, 1, 0, 0, 0, 0, TZ)
        to_entered_time = datetime(2025, 12, 31, 23, 59, 59, 999999, TZ)
        response = client.request(
            **client.ENDPOINTS["/orders"](from_entered_time, to_entered_time)
        )
        self.assertEqual(response.status_code, 200)

    def test_accounts_orders(self):
        """Test /accounts/{accountNumber}/orders"""
        from_entered_time = datetime(2025, 1, 1, 0, 0, 0, 0, TZ)
        to_entered_time = datetime(2025, 12, 31, 23, 59, 59, 999999, TZ)
        for account_number in self.account_numbers:
            response = client.request(
                **client.ENDPOINTS["/accounts/{accountNumber}/orders"](
                    account_number["hashValue"], from_entered_time, to_entered_time
                )
            )
            self.assertEqual(response.status_code, 200)

    def test_accounts_order(self):
        """Test /accounts/{accountNumber}/orders/{orderId}"""
        from_entered_time = datetime(2025, 1, 1, 0, 0, 0, 0, TZ)
        to_entered_time = datetime(2025, 12, 31, 23, 59, 59, 999999, TZ)
        for account_number in self.account_numbers:
            response = client.request(
                **client.ENDPOINTS["/accounts/{accountNumber}/orders"](
                    account_number["hashValue"], from_entered_time, to_entered_time
                )
            )
            self.assertEqual(response.status_code, 200)
            orders = response.json()
            order = orders[0]
            if order:
                response = client.request(
                    client.ENDPOINTS["/accounts/{accountNumber}/orders/{orderId}"](
                        account_number["hashValue"], order["orderId"]
                    )
                )
                self.assertEqual(response.status_code, 200)
