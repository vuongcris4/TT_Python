import sqlite3


class MY_DB:
    def connect(self):
        self.conn = sqlite3.connect("student.db")

    def disconnect(self):
        self.conn.close()
    def create_table(self):
        self.sql_create_table = """
            CREATE TABLE IF NOT EXISTS students (
                id TEXT,
                name TEXT,
                math REAL,
                physics REAL,
                chemistry REAL
            );
        """
        self.result = self.conn.execute(self.sql_create_table)
   

    def insert_row(self, id, name, math, physics, chemistry):
        sql_insert = """INSERT INTO students VALUES (?, ?, ?, ?, ?);"""
        self.result = self.conn.execute(
            sql_insert, (id, name, math, physics, chemistry)
        )
        self.conn.commit()

    def load_table_student(self):
        self.query = "SELECT * FROM students"
        self.result = self.conn.execute(self.query)
        return self.result
        
