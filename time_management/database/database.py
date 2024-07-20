import psycopg2
from time_management.config import settings


def get_connection():
    connection = psycopg2.connect(database=settings.DB_NAME, user=settings.DB_USER, password=settings.DB_PASS,
                                  host=settings.DB_HOST)

    return connection


def sql_execute(query, values, callback_data=None):
    try:
        connection = get_connection()
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(query, values)

            if callback_data == 'get':
                return cursor.fetchone()
            elif callback_data == 'get all':
                return cursor.fetchall()

    except Exception as e:
        print("We caught a problem:", e)
