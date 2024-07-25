import os
import sqlite3
from config import Config

class SQLite(object):

    def __init__(self, db_file_path) -> None:
        self.db_file_path = db_file_path
        self.connection = sqlite3.connect(db_file_path)
        self.cur = self.connection.cursor()

    def commit(self) -> None:
        self.connection.commit()

    def create_table(self, *args) -> None:
        self.cur.execute(args)
        self.commit()

    def __del__(self) -> None:
        self.connection.close()

    def __enter__(self):
        return self.connection.cursor()
        
    def execute_insert(self, data) -> None:
        self.cur.execute(data)
        self.commit()

    def executemany_insert(self, data_set) -> None:
        self.cur.executemany(data_set)
        self.commit()

    def __exit__(self, ext_type, exc_value, traceback):
        self.cur.close()
        if isinstance(exc_value, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()
        self.connection.close()
