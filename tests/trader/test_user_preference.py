import unittest

from bargaineer.schwab import client


class TestUserPreference(unittest.TestCase):
    def test_user_preference(self):
        """Test /userPreference"""
        response = client.request(client.ENDPOINTS["/userPreference"]())
        self.assertEqual(response.status_code, 200)
