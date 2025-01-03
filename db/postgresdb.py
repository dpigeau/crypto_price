import json
import os
from typing import Dict
import psycopg2

class postgresDB:
    def __init__(self):
        self.conn = psycopg2.connect(
            database=os.getenv('POSTGRES_DB'),
            host="localhost",
            user=os.getenv('POSTGRES_USER'),
            password=os.getenv('POSTGRES_PASSWORD'),
            port=os.getenv('POSTGRES_PORT'),
        )
        self.cursor = self.conn.cursor()

    def insert_rows(self, table_name:str, row_data: Dict):
        sql_query = f"INSERT INTO {table_name} (row_data) VALUES ('{json.dumps(row_data)}'::jsonb);"
        self.cursor.execute(sql_query)
        self.conn.commit()
    
    def read_rows(self, table_name:str):
        sql_query = f"SELECT * FROM {table_name};"
        self.cursor.execute(sql_query)
        rows = self.cursor.fetchall()
        return rows

    def close(self):
        self.conn.close()
