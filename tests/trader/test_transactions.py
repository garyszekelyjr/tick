import unittest

from datetime import datetime

from bargaineer import TZ
from bargaineer.schwab import client


class TestTransactions(unittest.TestCase):
    def setUp(self) -> None:
        response = client.request(client.ENDPOINTS["/accounts/accountNumbers"]())
        self.assertEqual(response.status_code, 200)
        self.account_numbers = response.json()

    def test_transactions(self):
        """Test /accounts/{accountNumber}/transactions"""
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
        """Test /accounts/{accountNumber}/transactions/{transactionId}"""
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
