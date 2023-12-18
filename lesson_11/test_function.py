import unittest
from function import get_average_price


class TestAveragePrice(unittest.TestCase):

    def test_get_average_price_positive(self):
        """Test positive case for average price function"""
        journal_list = [
            {"name": "Space", "volume": 20000, "price": 12.45},
            {"name": "SeaSide", "volume": 5000, "price": 10.45},
            {"name": "Fortune", "volume": 10000, "price": 17.99},
            {"name": "Vouge", "volume": 25000, "price": 7.68},
        ]
        volume = 10000
        expected_result = 10.065
        actual_result = get_average_price(journal_list, volume)
        self.assertEqual(expected_result, actual_result, f"Expected result: "
                                                         f"{expected_result}, actual result: {actual_result}")

    def test_get_average_price_empty_result(self):
        """Test average price function when there is no journals with given volume"""
        journal_list = [
            {"name": "Space", "volume": 20000, "price": 12.45},
            {"name": "SeaSide", "volume": 5000, "price": 10.45},
            {"name": "Fortune", "volume": 10000, "price": 17.99},
            {"name": "Vouge", "volume": 25000, "price": 7.68},
        ]
        volume = 50000
        expected_result = 0
        actual_result = get_average_price(journal_list, volume)
        self.assertEqual(expected_result, actual_result, f"Expected result: "
                                                         f"{expected_result}, actual result: {actual_result}")

    def test_get_average_price_empty_list_given(self):
        """Test average price function when list is empty"""
        journal_list = []
        volume = 10000
        expected_result = 0
        actual_result = get_average_price(journal_list, volume)
        self.assertEqual(expected_result, actual_result, f"Expected result: "
                                                         f"{expected_result}, actual result: {actual_result}")


if __name__ == "__main__":
    unittest.main(verbosity=2)