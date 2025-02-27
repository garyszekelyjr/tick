import unittest

from datetime import datetime

from bargaineer import TZ
from bargaineer.schwab import client


class TestAccounts(unittest.TestCase):
    def test_account_numbers(self):
        response = client.request(client.ENDPOINTS["/accounts/accountNumbers"]())
        self.assertEqual(response.status_code, 200)

    def test_accounts(self):
        response = client.request(client.ENDPOINTS["/accounts"]())
        self.assertEqual(response.status_code, 200)

    def test_account(self):
        response = client.request(client.ENDPOINTS["/accounts/accountNumbers"]())
        self.assertEqual(response.status_code, 200)
        account_numbers = response.json()
        for account_number in account_numbers:
            response = client.request(
                client.ENDPOINTS["/accounts/{accountNumber}"](
                    account_number["hashValue"]
                )
            )
            self.assertEqual(response.status_code, 200)


class TestOrders(unittest.TestCase):
    def setUp(self) -> None:
        response = client.request(client.ENDPOINTS["/accounts/accountNumbers"]())
        self.assertEqual(response.status_code, 200)
        self.account_numbers = response.json()

    def test_orders(self):
        from_entered_time = datetime(2025, 1, 1, 0, 0, 0, 0, TZ)
        to_entered_time = datetime(2025, 12, 31, 23, 59, 59, 999999, TZ)
        response = client.request(
            **client.ENDPOINTS["/orders"](from_entered_time, to_entered_time)
        )
        self.assertEqual(response.status_code, 200)

    def test_accounts_orders(self):
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


class TestTransactions(unittest.TestCase):
    def setUp(self) -> None:
        response = client.request(client.ENDPOINTS["/accounts/accountNumbers"]())
        self.assertEqual(response.status_code, 200)
        self.account_numbers = response.json()

    def test_transactions(self):
        start_date = datetime(2025, 1, 1, 0, 0, 0, 0, TZ)
        end_date = datetime(2025, 12, 31, 23, 59, 59, 999999, TZ)
        for account_number in self.account_numbers:
            response = client.request(
                **client.ENDPOINTS["/accounts/{accountNumber}/transactions"](
                    account_number["hashValue"], start_date, end_date
                )
            )
            self.assertEqual(response.status_code, 200)

    def test_transaction(self):
        start_date = datetime(2025, 1, 1, 0, 0, 0, 0, TZ)
        end_date = datetime(2025, 12, 31, 23, 59, 59, 999999, TZ)
        for account_number in self.account_numbers:
            response = client.request(
                **client.ENDPOINTS["/accounts/{accountNumber}/transactions"](
                    account_number["hashValue"], start_date, end_date
                )
            )
            self.assertEqual(response.status_code, 200)
            transactions = response.json()
            transaction = transactions[0]
            if transaction:
                response = client.request(
                    client.ENDPOINTS[
                        "/accounts/{accountNumber}/transactions/{transactionId}"
                    ](account_number["hashValue"], transaction["activityId"])
                )
                self.assertEqual(response.status_code, 200)
