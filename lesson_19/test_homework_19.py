import unittest
from homework_19 import SQLiteDB
from pathlib import Path


class TestSQLiteDB(unittest.TestCase):

    def test_init(self):
        """Test initiation of the class SQLiteDB and creating a table"""
        db_name = 'test_database'
        SQLiteDB(db_name)
        self.assertTrue(if_file_exists(Path.cwd(), db_name))
        delete_file(Path.cwd(), db_name)

    def test_create_table(self):
        """Test creating a table"""
        db_name = 'test_database'
        table_name = "test_table"
        columns = ["id INTEGER", "name TEXT", "age INTEGER"]
        db = SQLiteDB(db_name)
        db.create_table(table_name, columns)

        query = f"PRAGMA table_info({table_name})"
        db.cursor.execute(query)
        table_info = db.cursor.fetchall()

        self.assertEqual(len(table_info), len(columns))
        delete_file(Path.cwd(), db_name)

    def test_insert_to_table(self):
        """Test inserting data to the table"""
        db_name = 'test_database'
        table_name = "test_table"
        columns = ["id INTEGER", "name TEXT", "age INTEGER"]
        db = SQLiteDB(db_name)
        db.create_table(table_name, columns)

        data = {"id": 1, "name": "John Doe", "age": 25}
        db.insert_to_table(table_name, data)

        query = f"SELECT * FROM {table_name}"
        db.cursor.execute(query)
        result = db.cursor.fetchone()

        self.assertEqual(result, (1, "John Doe", 25))
        delete_file(Path.cwd(), db_name)

    def test_select_all_from_table(self):
        """Test function that selects all data from table"""
        db_name = 'test_database'
        table_name = "test_table"
        columns = ["id INTEGER", "name TEXT", "age INTEGER"]
        db = SQLiteDB(db_name)
        db.create_table(table_name, columns)

        data = {"id": 1, "name": "John Doe", "age": 25}
        db.insert_to_table(table_name, data)

        result = db.select_all_from_table(table_name)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], (1, "John Doe", 25))
        delete_file(Path.cwd(), db_name)

    def test_create_table_from_csv(self):
        csv_file_path = "test_csv_data.csv"
        with open(csv_file_path, "w", encoding="utf-8") as csvfile:
            csvfile.write("id,name,age\n1,John Doe,25\n2,Jane Smith,30\n")

        db_name = 'test_database'
        db = SQLiteDB(db_name)
        db.create_table_from_csv(Path(csv_file_path))

        query = f"PRAGMA table_info({csv_file_path.rstrip('.csv')})"
        db.cursor.execute(query)
        table_info = db.cursor.fetchall()
        self.assertEqual(len(table_info), 3)

        query = "SELECT * FROM test_csv_data"
        db.cursor.execute(query)
        result = db.cursor.fetchall()

        self.assertEqual(len(result), 2)
        delete_file(Path.cwd(), csv_file_path)
        delete_file(Path.cwd(), db_name)

    def test_delete_from_table(self):
        """Test deleting row from the table"""
        db_name = 'test_database'
        table_name = "test_table"
        columns = ["id INTEGER", "name TEXT", "age INTEGER"]
        db = SQLiteDB(db_name)
        db.create_table(table_name, columns)

        data = {"id": 1, "name": "John Doe", "age": 25}
        db.insert_to_table(table_name, data)

        condition = "id = 1"
        db.delete_from_table(table_name, condition)

        query = f"SELECT * FROM {table_name}"
        db.cursor.execute(query)
        result = db.cursor.fetchall()

        self.assertEqual(len(result), 0)
        delete_file(Path.cwd(), db_name)


def if_file_exists(path, file_name):
    my_file = path / file_name
    return my_file.is_file()


def delete_file(path, file_name):
    my_file = path / file_name
    if my_file.is_file():
        my_file.unlink()


if __name__ == '__main__':
    unittest.main()
