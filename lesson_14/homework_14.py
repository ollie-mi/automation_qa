"""
Створіть class SiteUser() для представлення користувача в системі.
Кожен користувач має ім'я, електронну пошту та рівень доступу (admin, moderator, user).
Також користувач має лічильник кількість логінів - logcount (int)
Реалізуйте необхідні методи та атрибути, використовуючи магічні методи для поліпшення
функціональності.

Вимоги:

    Клас Користувач має мати атрибути: ім'я, електронна_пошта, рівень_доступу, кількість логінів (logcount).
    Реалізуйте методи для отримання та встановлення значень атрибутів (гетери та сетери).
    Перевизначте метод __str__, щоб при виведенні об'єкта на екран 
    виводилася інформація про користувача.
    Реалізуйте метод __eq__, який дозволяє порівнювати два об'єкта за рівнем доступу.
    Реалізуйте щоб SiteUser.logcount можна було збільшувати

Приклад використання:

user1 = Користувач("John Doe", "john.doe@example.com", "user")
user2 = Користувач("Jane Smith", "jane.smith@example.com", "admin")

print(user1)
# Виведе: Користувач: John Doe, Електронна пошта: john.doe@example.com, Рівень доступу: user

# Порівняння користувачів
if user1 == user2:
    print("Користувачі однакові")
else:
    print("Користувачі різні")

Написати на це все тести
"""
import re


class SiteUser:
    """Class for representing user login to the system"""

    def __init__(self, name, email, access_level):
        self.__name = name
        self.__email = email
        self.__access_level = access_level
        self.__logcount = 0
        self.__levels = ['admin', 'moderator', 'user']

    @property
    def name(self):
        """Getter for attribute name"""
        return self.__name

    @name.setter
    def name(self, new_name: str):
        """Setter for attribute name"""
        if not isinstance(new_name, str):
            raise ValueError("Name should be a string")
        self.__name = new_name

    @property
    def email(self):
        """Getter for attribute email"""
        return self.__email

    @email.setter
    def email(self, new_email):
        """Setter for attribute email"""
        if not re.match(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+$", new_email):
            raise ValueError("Email address is not valid")
        self.__email = new_email

    @property
    def access_level(self):
        """Getter for attribute access_level"""
        return self.__access_level

    @access_level.setter
    def access_level(self, new_level):
        """Setter for attribute access_level"""
        if new_level not in self.__levels:
            raise ValueError("Such level doesn't exists")
        self.__access_level = new_level

    @property
    def logcount(self):
        """Getter for attribute logcounter"""
        return self.__logcount

    @logcount.setter
    def logcount(self, new_logcount):
        """Setter for attribute logcounter"""
        if not isinstance(new_logcount, int):
            raise ValueError("Log Counter should be integer")
        self.__logcount = new_logcount

    @classmethod
    def increase_logcount(cls, user):
        """Increase log counter for the user"""
        user.logcount += 1

    def __str__(self):
        return str(f"Користувач: {self.name}, Електронна пошта: {self.email}, Рівень доступу: {self.access_level}")

    def __eq__(self, other):
        if isinstance(other, SiteUser):
            return self.__access_level == other.__access_level
        return False


if __name__ == '__main__':
    user1 = SiteUser("John Doe", "john.doe@example.com", "user")
    user2 = SiteUser("Jane Smith", "jane.smith@example.com", "admin")
    user3 = SiteUser("John Kennedy", "john.kennedy@example.com", "user")
    print(user1)

    if user1 == user2:
        print("Користувачі однакові")
    else:
        print("Користувачі різні")
