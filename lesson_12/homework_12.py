from lesson_10.logger import logger
from pathlib import Path
import csv
import json
import xml.etree.ElementTree as ET

CURRENT_FILE_PATH = Path(__file__)
TEST_FILES_DIR = CURRENT_FILE_PATH.parent.parent / "ideas_for_test"
CURRENT_DIR = Path.cwd()

# task 1
""" Візміть два файли з теки
ideas_for_test/work_with_csv
порівняйте на наявність дублікатів
результат запишіть у файл result_<your_second_name>.csv
"""


def get_duplicate_csv(csv_name_1: str, csv_name_2: str) -> None:
    """
    Function takes two csv files, compares content and creates new csv file with duplicates
    """
    csv_dir = TEST_FILES_DIR / 'work_with_csv'
    file_1_path = csv_dir / csv_name_1
    file_2_path = csv_dir / csv_name_2

    if file_1_path.suffix != ".csv" or file_2_path.suffix != ".csv":
        raise ValueError(f"{csv_name_1} or {csv_name_2} should be csv files")
    if not file_1_path.exists():
        raise FileNotFoundError(f"File {csv_name_1} was not found in {csv_dir}")
    if not file_2_path.exists():
        raise FileNotFoundError(f"File {csv_name_2} was not found in {csv}")

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


# task 2
""" Провалідуйте, чи усі файли у папці
ideas_for_test/work_with_json
є валідними json.
результат для невалідного файлу виведіть через логер на рівні еррор
"""


def is_valid_json_in_dir(json_dir) -> None:
    """
    Function iterates all json files in the directory and validates it
    Outputs invalid json file information to the logger at ERROR level.
    """
    json_files_list = [x for x in json_dir.glob('*.json')]
    if json_files_list:
        for jsonfile in json_files_list:
            with jsonfile.open("r", encoding="utf-8") as file:
                try:
                    name = jsonfile.name
                    json_data = json.loads(file.read())
                except json.decoder.JSONDecodeError:
                    logger.error(f"File {name} is not valid json file")


# task 3
""" Для файла ideas_for_test/work_with_xml/groups.xml
створіть функцію  пошуку по group/number і далі
по значенню timingExbytes/incoming
результат пошуку виведіть через логер на рівні інфо
"""


def find_group_and_value_in_xml(xml_file: str, group_number: int, incoming_value: str) -> None:
    """
    Function searches specified group number and 'timingExbytes/incoming' attribute.
    Outputs the matching group information to the logger at INFO level.
    """
    xml_dir = TEST_FILES_DIR / "work_with_xml"
    xml_file = xml_dir / xml_file

    if xml_file.suffix != ".xml":
        raise ValueError(f"{xml_file} should be xml file")
    if not xml_file.exists():
        raise FileNotFoundError(f"File {xml_file} was not found in {xml_dir}")

    with xml_file.open() as xmlfile:
        xml_content = xmlfile.read()

    root = ET.fromstring(xml_content)

    groups = root.findall(f".//group[number='{group_number}']")
    if groups:
        for group in groups:
            timing_exbytes = group.find('timingExbytes')
            if timing_exbytes:
                incoming_attribute = timing_exbytes.find('incoming')
                if incoming_attribute is not None:
                    if incoming_attribute.text == incoming_value:
                        logger.info(f"Group {group_number} with incoming value {incoming_value} found")
                        return
                    else:
                        logger.info(f"Group {group_number} with incoming value {incoming_value} not found")
                else:
                    logger.info(f"Group {group_number} doesn't have 'incoming' attribute")
            else:
                logger.info(f"Group {group_number} doesn't have 'timingExbytes' attribute")
    else:
        logger.info(f"Group {group_number} does not exist")


if __name__ == '__main__':
    get_duplicate_csv('rmc.csv', 'r-m-c.csv')

    json_files_dir = TEST_FILES_DIR / "work_with_json"
    is_valid_json_in_dir(json_files_dir)

    find_group_and_value_in_xml('groups.xml', 2, '0xACDC')
