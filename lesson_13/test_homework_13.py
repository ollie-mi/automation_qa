import unittest
from homework_13 import Human


class TestHuman(unittest.TestCase):
    def test_init(self):
        """Test initiation of the class Human"""
        human = Human("Frodo", "Baggins", "22.09.2968", "male")
        self.assertEqual(human.name, "Frodo")
        self.assertEqual(human.last_name, "Baggins")
        self.assertEqual(human.birth_date, "22.09.2968")
        self.assertEqual(human.gender, "male")
        self.assertEqual(human.energy, 100)

    def test_eat(self):
        """Test function eat from class Human"""
        human = Human("Frodo", "Baggins", "22.09.2968", "male")
        human.eat()
        self.assertEqual(human.energy, 105)

    def test_sleep(self):
        """Test function sleep from class Human"""
        human = Human("Frodo", "Baggins", "22.09.2968", "male")
        human.sleep()
        self.assertEqual(human.energy, 110)

    def test_speak(self):
        """Test function speak from class Human"""
        human = Human("Frodo", "Baggins", "22.09.2968", "male")
        human.speak()
        self.assertEqual(human.energy, 95)

    def test_walk(self):
        """Test function walk from class Human"""
        human = Human("Frodo", "Baggins", "22.09.2968", "male")
        human.walk()
        self.assertEqual(human.energy, 90)

    def test_do_homework(self):
        """Test function do_homework from class Human"""
        human = Human("Frodo", "Baggins", "22.09.2968", "male")
        human.do_homework()
        self.assertEqual(human.energy, 10)

    def test_empty_list(self):
        """Test empty list for function compare_energy of class Human"""
        human_list = []
        with self.assertRaises(ValueError):
            result = Human.compare_energy(human_list)

    def test_one_human(self):
        """Test list with only one human for function compare_energy of class Human"""
        human_list = [Human("Frodo", "Baggins", "22.09.2968", "male")]
        result = Human.compare_energy(human_list)

        self.assertEqual("Frodo", result.name)
        self.assertEqual("Baggins", result.last_name)
        self.assertEqual(100, result.energy)

    def test_multiple_humans(self):
        """Test list with multiple humans for function compare_energy of class Human"""
        human_list = [
            Human("Frodo", "Baggins", "22.09.2968", "male"),
            Human("Bilbo", "Baggins", "22.09.2890", "male"),
            Human('Hermione', 'Granger', '19.09.1979', 'female')
        ]
        human_list[0].walk()
        human_list[1].speak()

        result = Human.compare_energy(human_list)
        self.assertEqual("Hermione", result.name)
        self.assertEqual("Granger", result.last_name)
        self.assertEqual(100, result.energy)