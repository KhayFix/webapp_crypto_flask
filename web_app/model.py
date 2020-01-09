import psycopg2
from datetime import datetime

from web_app.config import database


def connection_to_base():
    conn = psycopg2.connect(database=database['database'],
                            user=database['user'],
                            password=database['password'],
                            host=database['host'],
                            port=database['port'],
                            )

    print("База данных успешно открыта")
    return conn


def retrieving_table_data(table_database: str):
    my_list = []
    with connection_to_base() as conn:
        with conn.cursor() as curs:
            curs.execute(
                f'''SELECT * FROM "{table_database}" '''
            )

            for record in curs:
                value = datetime.fromtimestamp(record[1])
                my_list.append({
                    "id": record[0],
                    "Timestamp": value.strftime('%d-%m-%Y %H:%M:%S'),
                    "Open": float(record[2]),
                    "Close": float(record[3]),
                    "High": float(record[4]),
                    "Low": float(record[5]),
                    "Volume": float(record[6])
                })

    print('Таблица успешно прочитана')
    conn.close()
    return my_list


if __name__ == "__main__":
    retrieving_table_data('crypto_project')
