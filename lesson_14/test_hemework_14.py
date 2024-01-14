import unittest
from homework_14 import SiteUser


class TestSiteUser(unittest.TestCase):

    def test_init(self):
        """Test initiation of the class SiteUser"""
        user = SiteUser("John Doe", "john.doe@example.com", "user")
        self.assertEqual(user.name, "John Doe")
        self.assertEqual(user.email, "john.doe@example.com")
        self.assertEqual(user.access_level, "user")

    def test_setters_getters(self):
        """Test getters and setters in class SiteUser"""
        user = SiteUser("John Doe", "john.doe@example.com", "user")

        user.name = "Tom Peterson"
        self.assertEqual(user.name, "Tom Peterson")

        user.email = "tom.peterson@example.com"
        self.assertEqual(user.email, "tom.peterson@example.com")

        user.access_level = "admin"
        self.assertEqual(user.access_level, "admin")

        user.logcount = 10
        self.assertEqual(user.logcount, 10)

    def test_invalid_email(self):
        """Test email setter for class SiteUser with invalid email"""
        user = SiteUser("John Doe", "john.doe@example.com", "user")
        with self.assertRaises(ValueError):
            user.email = "wrong.email"

    def test_invalid_access_level(self):
        """Test access_level setter for class SiteUser with invalid access level"""
        user = SiteUser("John Doe", "john.doe@example.com", "user")
        with self.assertRaises(ValueError):
            user.access_level = 'reader'

    def test_increase_logcount(self):
        """Test increase_logcount function for class SiteUser"""
        user = SiteUser("John Doe", "john.doe@example.com", "user")
        user.logcount = 10
        user.increase_logcount(user)
        self.assertEqual(user.logcount, 11)

    def test_str(self):
        """Test __str__ function for class SiteUser"""
        user = SiteUser("John Doe", "john.doe@example.com", "user")
        self.assertEqual(str(user), "Користувач: John Doe, Електронна пошта: john.doe@example.com, "
                                    "Рівень доступу: user")

    def test_eq(self):
        """Test __eq__ function for class SiteUser"""
        user1 = SiteUser("John Doe", "john.doe@example.com", "user")
        user2 = SiteUser("Jane Smith", "jane.smith@example.com", "admin")
        self.assertFalse(user1 == user2)

        user3 = SiteUser("John Doe", "john.doe@example.com", "user")
        self.assertTrue(user1 == user3)
