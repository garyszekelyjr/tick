import unittest

from bargaineer.schwab import client


class TestAccounts(unittest.TestCase):
    def test_account_numbers(self):
        """Test /accounts/accountNumbers"""
        response = client.request(client.ENDPOINTS["/accounts/accountNumbers"]())
        self.assertEqual(response.status_code, 200)

    def test_accounts(self):
        """Test /accounts"""
        response = client.request(client.ENDPOINTS["/accounts"]())
        self.assertEqual(response.status_code, 200)

    def test_account(self):
        """Test /accounts/{accountNumber}"""
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
