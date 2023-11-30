small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
# task 1. Знайдіть всі унікальні елементи в списку small_list

unique_small_list = set(small_list)
print(unique_small_list)

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list

average = sum(small_list)/len(small_list)
print(average)

# task 3. Перевірте, чи є в списку big_list дублікати

big_list_set = set(big_list)
if len(big_list) > len(big_list_set):
    print("big_list має дублікати")
else:
    print("дублікатів в big_list не знайдено")


base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict

max_key = max(add_dict)
print(max_key)

# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику

new_dict = {}
for key, value in base_dict.items():
    new_key = value if isinstance(value, str) else str(value)
    new_dict[new_key] = key

print(new_dict)

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх

sum_dict = base_dict.copy()
for key, value in add_dict.items():
    if key in sum_dict:
        sum_dict[key] = str(sum_dict[key]) + str(value)
    else:
        sum_dict[key] = value

print(sum_dict)

# task 7.
line = "Створіть множину всіх символів, які входять у заданий рядок"

line_set = set(line)
print(line_set)

# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}

merged_set = set_1 | set_2
intersection_set = set_1 & set_2
merger_sum = sum(merged_set)
for i in merged_set:
    if i in intersection_set:
        merger_sum -= i

print(merger_sum)

# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]

list_1 = [5, 3, 1, 8, 9]
list_2 = [7, 8, 5, 9, 13, 15]

symmetric_difference_set = set(list_1) ^ set(list_2)
print(symmetric_difference_set)


person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]
# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}

new_person_dict = {}
age_map = [[0, 9], [10, 19], [20, 29], [30, 39], [40, 49], [50, 59], [60, 69], [70, 79], [80, 89], [90, 99]]
for person in person_list:
    name, age = person
    for range_item in age_map:
        if range_item[0] <= age <= range_item[1]:
            key = f"{range_item[0]}-{range_item[1]}"
            if key in new_person_dict:
                new_person_dict[key].append(name)
            else:
                new_person_dict.update({key: [name]})

dict_keys = list(new_person_dict.keys())
dict_keys.sort()
new_person_dict_sorted = {i: new_person_dict[i] for i in dict_keys}

print(new_person_dict_sorted)
