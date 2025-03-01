import unittest

from bargaineer.schwab.trader import user_preference


class TestUserPreference(unittest.TestCase):
    def test_user_preference(self):
        """Test /userPreference"""
        response = user_preference.get()
        self.assertEqual(response.status_code, 200)
