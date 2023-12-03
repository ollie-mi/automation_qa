# task 1
"""  Уявіть, що інопланетянина з кольором alien_color щойно збили в грі.
Створіть змінну під назвою alien_color і призначте їй значення 'green', 'yellow', або 'red'.
Напишіть оператор if, щоб перевірити, чи колір прибульця 'green'.
Якщо так, надрукуйте повідомлення про те, що гравець щойно заробив 5 балів.
"""

alien_color = 'green'
if alien_color == 'green':
    print("Congratulations! You just won 5 points")

# task 2
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою else.
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Зробіть так, щоб виводилася умова else.
"""

alien_color = 'red'
if alien_color == 'green':
    print("Congratulations! You just won 5 points")
else:
    print("Congratulations! You just won 10 points")

# task 3
# task 4
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою elif.
змінну під назвою alien_color перетворіть у список значень: 'green', 'yellow', 'red'
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Якщо прибулець червоний, надрукуйте повідомлення про те, що гравець заробив 15 очок
+ напишіть цикл for що перебере і обробить всі значення списку alien_color
"""

alien_color = ['green', 'yellow', 'red']

for color in alien_color:
    if color == 'green':
        print("Congratulations! You just won 5 points")
    elif color == 'red':
        print("Congratulations! You just won 15 points")
    else:
        print("Congratulations! You just won 10 points")

# task 5
"""  Начинки для піци (pizza_topping): напишіть цикл, який пропонує користувачеві ввести ряд начинок
для піци, доки він не введе значення 'quit'. Коли вони введуть кожну начинку,
надрукуйте повідомлення про те, що ви додасте цю начинку до їхньої піци.
"""

pizza_topping = ''
while pizza_topping != 'quit':
    pizza_topping = input("Please, write what you want to add to your pizza or write 'quit' to finish ")
    if pizza_topping != 'quit':
        print(f"We will add {pizza_topping} to your pizza")
print("Your pizza is getting ready!")

# task 6
"""  Напишіть програму, яка знаходить суму всіх цифр натурального числа, яке вводить користувач.
Для перебору вводу від користувача використовуйте цикл. Виведіть суму цифр числа на екран.
Приклад виконання програми:
Введіть натуральне число: 12345
Сума цифр числа 12345: 15
"""

numbers_input = input("Введіть натуральне число: ")
sum_numbers = 0
for number in numbers_input:
    if number.isdigit():
        sum_numbers += int(number)
print(f"Сума цифр числа {numbers_input}: {sum_numbers}")

# task 7
"""  Потрібно написати програму, яка просить користувача ввести числа, доки він не введе 0.
Програма повинна підрахувати суму всіх введених чисел, окрім 0, і вивести її на екран.
Це повинно працювать як калькулятор, в який ввів цифру - нажав плюс - ввів наступну цифру.
Після введеня 0 показує результат сумування.
Розв'язати з використанням циклу while та break
"""

total = 0
while True:
    add_number = input("Введіть число: ")
    if add_number == '0':
        break
    if add_number.isdigit():
        total += int(add_number)
print(f"Сума всіх введенних чисел: {total}")


# task 8
"""  З використанням циклу for реалізуйте гру "Вгадай число".
Початок програми написаний, гравець має 5 спроб відгадати випадкове число від 1 до 20,
яке було згенеровано за допомогою функції randint() модуля random.
У кожній спробі гравець вводить своє припущення, після чого програма повідомляє, чи
було припущення занадто великим або занадто малим, чи гравець вгадав число.
"""
import random
secret_number = random.randint(1, 20)
guesses = 0
max_guesses = 5
print("Вгадайте число від 1 до 20 за 5 спроб!")

for guesses in range(1, max_guesses + 1):
    guessed_number = input("Вгадайте число: ")

    if int(guessed_number) < secret_number:
        print("Число занадто мале. Спробуйте ще раз")
    elif int(guessed_number) > secret_number:
        print("Число занадто велике. Спробуйте ще раз")
    else:
        print(f"Правильно! Загадене число {guessed_number}")
        break

    if guesses == max_guesses:
        print(f"Ви не вгадали. Було загадано число {secret_number}. Спробуйте зіграти ще")

# task 9
"""  Задача з використанням циклу for та continue. Задано список фруктів 'fruits'
потрібно вивести на екран всі елементи списку, окрім "orange".
"""
fruits = ["apple", "banana", "orange", "grape", "mango"]

for fruit in fruits:
    if fruit == 'orange':
        continue
    print(fruit)

# task 10
"""  Задано список чисел numbers, потрібно знайти список квадратів
парних чисел зі списку. Спробуйте використати if та цикл for в один рядок.
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [x ** 2 for x in numbers if x % 2 == 0]
print(result)  #  [4, 16, 36, 64, 100]
