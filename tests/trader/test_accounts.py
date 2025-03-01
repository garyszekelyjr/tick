import unittest

from bargaineer.schwab.trader import accounts


class TestAccounts(unittest.TestCase):
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
