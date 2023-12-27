from pathlib import Path
import csv

CURRENT_FILE_PATH = Path(__file__)
TEST_FILE_DIR = CURRENT_FILE_PATH.parent.parent / "ideas_for_test" / "work_with_csv"
CURRENT_DIR = Path.cwd()

# task 1
""" Візміть два файли з теки
ideas_for_test/work_with_csv
порівняйте на наявність дублікатів
результат запишіть у файл result_<your_second_name>.csv
"""


def get_duplicate_csv(csv_name_1: str, csv_name_2: str) -> None:
    """Function takes two csv files, compares content and creates new csv file with duplicates"""
    file_1_path = TEST_FILE_DIR / csv_name_1
    file_2_path = TEST_FILE_DIR / csv_name_2

    if file_1_path.suffix != ".csv" or file_2_path.suffix != ".csv":
        raise ValueError(f"{csv_name_1} or {csv_name_2} should be csv files")
    if not file_1_path.exists():
        raise FileNotFoundError(f"File {csv_name_1} was not found in {TEST_FILE_DIR}")
    if not file_2_path.exists():
        raise FileNotFoundError(f"File {csv_name_2} was not found in {TEST_FILE_DIR}")

    with file_1_path.open("r", encoding="utf-8") as csvfile_1:
        dialect = csv.Sniffer().sniff(csvfile_1.read(1024))
        csvfile_1.seek(0)
        csv_data_1 = list(csv.reader(csvfile_1, dialect))
        csv_data_1 = [[x.replace(';', ',') for x in l] for l in csv_data_1]

    with file_2_path.open("r", encoding="utf-8") as csvfile_2:
        dialect = csv.Sniffer().sniff(csvfile_2.read(1024))
        csvfile_2.seek(0)
        csv_data_2 = list(csv.reader(csvfile_2, dialect))
        csv_data_2 = [[x.replace(';', ',') for x in l] for l in csv_data_2]

    duplicate_rows = []
    for row in csv_data_1:
        if row in csv_data_2:
            duplicate_rows.append(row)

    if duplicate_rows:
        new_duplicate_file = CURRENT_DIR / "result_mialkivska.csv"

        with open(new_duplicate_file, "w", encoding="utf-8") as duplicate_file:
            duplicate_writer = csv.writer(duplicate_file, delimiter=";", quotechar='"')
            duplicate_writer.writerows(duplicate_rows)


get_duplicate_csv('rmc.csv', 'r-m-c.csv')


# task 2
""" Провалідуйте, чи усі файли у папці
ideas_for_test/work_with_json
є валідними json.
результат для невалідного файлу виведіть через логер на рівні еррор
"""


# task 3
""" Для файла ideas_for_test/work_with_xml/groups.xml
створіть функцію  пошуку по group/number і далі
по значенню timingExbytes/incoming
результат пошуку виведіть через логер на рівні інфо
"""

