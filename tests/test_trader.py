import unittest

from datetime import datetime

from tick import TZ
from tick.schwab.trader import accounts, orders, transactions, user_preference


class TestTrader(unittest.TestCase):
    def setUp(self) -> None:
        response = accounts.account_numbers()
        self.assertEqual(response.status_code, 200)
        self.account_numbers = response.json()

    def test_account_numbers(self):
        """Test /accounts/accountNumbers"""
        response = accounts.account_numbers()
        self.assertEqual(response.status_code, 200)

    def test_accounts(self):
        """Test /accounts"""
        response = accounts.get_all()
        self.assertEqual(response.status_code, 200)

    def test_account(self):
        """Test /accounts/{accountNumber}"""
        response = accounts.account_numbers()
        self.assertEqual(response.status_code, 200)
        account_numbers = response.json()
        for account_number in account_numbers:
            response = accounts.get(account_number["hashValue"])
            self.assertEqual(response.status_code, 200)

    def test_orders(self):
        """Test /orders"""
        from_entered_time = datetime(2025, 1, 1, 0, 0, 0, 0, TZ)
        to_entered_time = datetime(2025, 12, 31, 23, 59, 59, 999999, TZ)
        response = orders.orders(from_entered_time, to_entered_time)
        self.assertEqual(response.status_code, 200)

    def test_accounts_orders(self):
        """Test /accounts/{accountNumber}/orders"""
        from_entered_time = datetime(2025, 1, 1, 0, 0, 0, 0, TZ)
        to_entered_time = datetime(2025, 12, 31, 23, 59, 59, 999999, TZ)
        for account_number in self.account_numbers:
            response = orders.accounts_orders(
                account_number["hashValue"], from_entered_time, to_entered_time
            )
            self.assertEqual(response.status_code, 200)

    def test_accounts_order(self):
        """Test /accounts/{accountNumber}/orders/{orderId}"""
        from_entered_time = datetime(2025, 1, 1, 0, 0, 0, 0, TZ)
        to_entered_time = datetime(2025, 12, 31, 23, 59, 59, 999999, TZ)
        for account_number in self.account_numbers:
            response = orders.accounts_orders(
                account_number["hashValue"], from_entered_time, to_entered_time
            )
            self.assertEqual(response.status_code, 200)
            order = response.json()[0]
            if order:
                response = orders.accounts_order(
                    account_number["hashValue"], order["orderId"]
                )
                self.assertEqual(response.status_code, 200)

    def test_transactions(self):
        """Test /accounts/{accountNumber}/transactions"""
        start_date = datetime(2025, 1, 1, 0, 0, 0, 0, TZ)
        end_date = datetime(2025, 12, 31, 23, 59, 59, 999999, TZ)
        for account_number in self.account_numbers:
            response = transactions.get_all(
                account_number["hashValue"], start_date, end_date
            )
            self.assertEqual(response.status_code, 200)

    def test_transaction(self):
        """Test /accounts/{accountNumber}/transactions/{transactionId}"""
        start_date = datetime(2025, 1, 1, 0, 0, 0, 0, TZ)
        end_date = datetime(2025, 12, 31, 23, 59, 59, 999999, TZ)
        for account_number in self.account_numbers:
            response = transactions.get_all(
                account_number["hashValue"], start_date, end_date
            )
            self.assertEqual(response.status_code, 200)
            transaction = response.json()[0]
            if transaction:
                response = transactions.get(
                    account_number["hashValue"], transaction["activityId"]
                )
                self.assertEqual(response.status_code, 200)

    def test_user_preference(self):
        """Test /userPreference"""
        response = user_preference.get()
        self.assertEqual(response.status_code, 200)
