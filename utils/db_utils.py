import pymysql

from utils.read_config import ReadConfig


class DBUtils:
    @staticmethod
    def get_connection():
        try:
            conn = pymysql.connect(
                host=ReadConfig.get_db_host(),
                user=ReadConfig.get_db_user(),
                password=ReadConfig.get_db_password(),
                database=ReadConfig.get_db_name()
            )
            print("Connected Successfully")
            return conn
        except Exception as e:
            raise RuntimeError (f'Error connecting to db {e}')

    @staticmethod
    def execute_query(query):
        conn = DBUtils.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query)
            return cursor.fetchall()
        finally:
            cursor.close()
            conn.close()

