"""Розробити клас Human.
Людина має:
    Ім'я
    Прізвище
    Дату народження
    Стать
    Енергію = 100
Люди можуть:
    Їсти (Енергія +5)
    Спати (Енергія +10)
    Говорити (Енергія -5)
    Ходити (Енергія -10)
    Робити домашку (Енергія -90)
if __name__ == "__main__":
    Створити 3 чоловіків та 2 жінок, Задати кожному з них виконання
    декількох дій, вивести в кого найбільше енергії лишилося.
Створити тести на клас та на атрибути класу.
"""


class Human:

    def __init__(self, name, last_name, birth_date, gender) -> None:
        self.name = name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.energy = 100

    def eat(self):
        """Increase energy by eating"""
        self.energy += 5

    def sleep(self):
        """Increase energy by sleeping"""
        self.energy += 10

    def speak(self):
        """Decrease energy by speaking"""
        self.energy -= 5

    def walk(self):
        """Decrease energy by walking"""
        self.energy -= 10

    def do_homework(self):
        """Decrease energy by doing homework"""
        self.energy -= 90

    @staticmethod
    def compare_energy(human_list: list):
        """Function returns human that has max energy"""
        winner = None
        if not human_list:
            raise ValueError("List of humans should not be empty")
        max_energy = 0
        for human in human_list:
            if human.energy > max_energy:
                max_energy = human.energy
                winner = human
        return winner


if __name__ == "__main__":
    man_1 = Human('Jack', 'Sparrow', '15.07.1690', 'male')
    man_1.eat()
    man_1.speak()
    man_1.walk()

    man_2 = Human('Luke', 'Skywalker', '06.10.7977', 'male')
    man_2.do_homework()
    man_2.sleep()
    man_2.eat()

    man_3 = Human('Harry', 'Potter', '31.07.1980', 'male')
    man_3.walk()
    man_3.speak()
    man_3.eat()
    man_3.sleep()
    man_3.do_homework()

    woman_1 = Human('Hermione', 'Granger', '19.09.1979', 'female')
    woman_1.do_homework()
    woman_1.walk()
    woman_1.eat()
    woman_1.speak()
    woman_1.eat()

    woman_2 = Human('Princess', 'Leia', '06.10.7977', 'female')
    woman_2.speak()
    woman_2.eat()
    woman_2.walk()

    men = [man_1, man_2, man_3]
    women = [woman_1, woman_2]

    energy_result = Human.compare_energy(men + women)
    print(f"{energy_result.name} {energy_result.last_name} has the biggest energy value: {energy_result.energy}")
