""" Оберіть від 3 до 5 різних домашніх завдань
- перетворюєте їх у функції (якщо це потрібно)
- створіть в папці файл homeworks.py куди вставте ваші функції з дз
- та покрийте їх не менш ніж 10 тестами (це загальна к-сть на все ДЗ).
-- імпорт та самі тести помістіть в окремому файлі - test_homeworks08.py
Код закомітьте в гіт, надайте посилання.
На оцінку впливає як якість тестів так і розмір тестового покриття.
Мінімум на 10 балів - 1 правильно задизайнений позитивний тест на функцію.
"""

import unittest
from lesson_07.homework_07 import *


class BasicFunctionsTesting(unittest.TestCase):

    def test_even_numbers_squares_positive(self):
        """Positive test of generating a list of squares for even numbers in the given list"""
        given_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected_list = [4, 16, 36, 64, 100]
        actual_result = even_numbers_squares(given_list)

        self.assertIsInstance(actual_result, list, "Function even_numbers_squares should return the list")
        self.assertListEqual(expected_list, actual_result, f"Given list {given_list}. List of squares for even "
                                                           f"numbers {actual_result}")

    def test_even_numbers_squares_empty_list(self):
        """Test raising exception for empty given list"""
        given_list = []
        with self.assertRaises(ValueError):
            even_numbers_squares(given_list)

    def test_even_numbers_squares_without_even(self):
        """Test returning empty list if given list doesn't have even numbers"""
        given_list = [3, 13, 17, 5, 7, 23, 31, 1]
        expected_list = []
        actual_result = even_numbers_squares(given_list)
        self.assertEqual(expected_list, actual_result, f"even_numbers_squares returns {actual_result} for list "
                                                       f"without even numbers")


if __name__ == "__main__":
    unittest.main(verbosity=2)
