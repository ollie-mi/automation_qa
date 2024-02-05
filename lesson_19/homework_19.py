import csv
import sqlite3
from pathlib import Path


class SQLiteDB:

    def __init__(self, db_name: str) -> None:
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_table(self, table_name: str, *args) -> None:
        """Create table with columns from the list"""
        columns_query = ''
        for arg in args:
            columns_query = ', '.join(arg)
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_query})"
        self.cursor.execute(query)
        self.connection.commit()

    def insert_to_table(self, table_name: str, data: dict) -> None:
        """Insert data to the table"""
        columns = []
        values = []
        for key, value in data.items():
            columns.append(key)
            values.append(value)
        columns_query = ', '.join(filter(None, columns))
        values_query = ', '.join(f"'{x}'" for x in values)
        query = f"INSERT INTO {table_name} ({columns_query}) VALUES ({values_query})"
        self.cursor.execute(query)
        self.connection.commit()

    def select_all_from_table(self, table_name: str) -> list:
        """Select all data from table"""
        query = f"SELECT * FROM {table_name}"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def create_table_from_csv(self, csv_file: Path) -> None:
        """Function receives path to the csv file, creates table that has name as file and columns as file header,
        inserts file data to the db"""
        table_name = csv_file.stem.replace('-', '')
        with csv_file.open("r", encoding="utf-8") as csvfile:
            data_read = list(csv.reader(csvfile, delimiter=",", quotechar='"'))
            columns_list = data_read.pop(0)
            i = 0
            for key, value in enumerate(columns_list):
                if not value:
                    columns_list[key] = f"TestName{i}"
                    i += 1
            self.create_table(table_name, columns_list)
            for row in data_read:
                for key, value in enumerate(row):
                    row[key] = value.replace("'", "")
                insert_dict = dict(zip(columns_list, row))
                self.insert_to_table(table_name, insert_dict)

    def delete_from_table(self, table_name: str, condition: str) -> None:
        """Delete row from the given table according to given conditions"""
        query = f"DELETE FROM {table_name} WHERE {condition}"
        self.cursor.execute(query)
        self.connection.commit()


if __name__ == "__main__":

    db = SQLiteDB("test_db")

    table_name = 'users'
    table_columns = ["id INTEGER PRIMARY KEY AUTOINCREMENT", "name TEXT", "last_name TEXT", "gender TEXT"]
    db.create_table(table_name, table_columns)

    insert_data = {'name': 'John', 'last_name': 'Dou', 'gender': 'male'}
    db.insert_to_table(table_name, insert_data)
    print(db.select_all_from_table(table_name))

    filename = Path(__file__).parent.parent / "ideas_for_test" / "work_with_csv" / "random-michaels.csv"
    db.create_table_from_csv(filename)

    condition = 'id = 1'
    db.delete_from_table(table_name, condition)
    print(db.select_all_from_table(table_name))
