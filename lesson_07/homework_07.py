# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""


def multiplication_table(number: int):
    """Prints multiplication table with max result of multiplication of 25"""
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1


# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""


def two_numbers_sum(num_1: int, num_2: int) -> int:
    """Calculate the sum of two numbers"""
    return num_1 + num_2


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""


def average_of_list_numbers(number_list: list) -> float:
    """Calculate arithmetic mean of list of numbers"""
    return sum(number_list) / len(number_list)


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""


def reverse_string(string: str) -> str:
    """Reverse the given string"""
    result_list = []
    for i in reversed(range(len(string))):
        result_list.append(string[i])
    result_string = ''.join(result_list)
    return result_string


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""


def longest_word_in_list(words_list: list) -> str:
    """Finds the longest word in the list"""
    longest_word = words_list[0]
    for word in words_list:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


capital_cities = ["Kyiv", "Wellington", "Reykjavik", "Zagreb", "Lisbon"]


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(str1: str, str2: str) -> int:
    """Finds position of string 1 in string 2. If fails to find, returns -1"""
    if str2 in str1:
        return str1.find(str2)
    else:
        return -1


# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""


def is_list_has_duplicates(ch_list: list) -> bool:
    """Checks the list for duplicates"""
    ch_set = set(ch_list)
    return len(ch_list) > len(ch_set)


big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]


def key_value_swapper(dictionary: dict) -> dict:
    """Swaps key and value in the dictionary"""
    new_dict = {}
    for key, value in dictionary.items():
        new_key = value if isinstance(value, str) else str(value)
        new_dict[new_key] = key
    return new_dict


base_dict = {'contry': 'Ukraine', 'continent': 'Europe', 'size': 123}


def pizza_constructor() -> list:
    """Adds toppings to pizza"""
    pizza_topping = ''
    toppings_list = []
    while pizza_topping != 'quit':
        pizza_topping = input("Please, write what you want to add to your pizza or write 'quit' to finish ")
        if pizza_topping != 'quit':
            toppings_list.append(pizza_topping)
            print(f"We will add {pizza_topping} to your pizza")
        if not toppings_list:
            toppings_list.append("just cheese")
    return toppings_list


def even_numbers_squares(num: list) -> list:
    """Generates a list of squares of even numbers from the list."""
    if not num:
        raise ValueError("Given list shouldn't be empty")
    return [x ** 2 for x in num if x % 2 == 0]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


if __name__ == "__main__":
    multiplication_table(3)
    print("3 + 5 =", two_numbers_sum(3, 5))
    print("Average of the list:", average_of_list_numbers([1, 2, 3, 4, 5, 6]))
    print("Reverse of Hello:", reverse_string('Hello'))
    print("Longest word in the list:", longest_word_in_list(capital_cities))

    str_1 = "Hello, world!"
    str_2 = "world"
    print(find_substring(str_1, str_2))  # поверне 7

    str_3 = "The quick brown fox jumps over the lazy dog"
    str_4 = "cat"
    print(find_substring(str_3, str_4))  # поверне -1

    print("Duplicate checker:", is_list_has_duplicates(big_list))
    print("Swap key and value in dict:", key_value_swapper(base_dict))

    toppings_str = ', '.join(pizza_constructor())
    print("Your pizza contains:", toppings_str)
    print("Even number squares:", even_numbers_squares(numbers))

