# Приклади виконання найпростіших команд із консолі інтерпретатора

# Створення найпростішої програми та збереження її у файл

# Запуск збереженого файлу на виконання

# Що таке IDE і навіщо воно треба
# print("Its error")
# Змінні (Variables), створення та використання змінних
# Заборонені символи у змінних
user_name = "Alex"
user_year_of_born = 2005
user_age = 16
print(user_name, user_year_of_born, user_age, sep=", ")
user_name = 'Viktoriya'
print(user_name)
print(user_year_of_born == user_age)
print(type(user_age))
# Відступи (Indentation)
if user_age == 18:
    print("Congratulations, you are no longer a teenager!")
    print("ok")
    if user_name:
        print("ssdd")
else:
    print("Not ok")
print("End of if")

# Найпростіші математичні операції:
# додавання, віднімання, множення
a = 5
b = 3

sum = a + b
dif = a - b
mult = a * b
div = a / b

# Вивід даних через print()
print(sum, dif, mult, div, sep="     ", end=" ")
print("End of lesson")