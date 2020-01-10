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


def data_conversion(database_data):
    my_list = []
    # преобразование данных к формату словаря полученных из базы данных
    for record in database_data:
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

    return my_list


def retrieving_table_data(database_table_title: str):
    with connection_to_base() as conn:
        with conn.cursor() as curs:
            curs.execute(
                f'''SELECT * FROM "{database_table_title}" '''
            )
            modified_data = data_conversion(curs)

    print('Таблица успешно прочитана')
    conn.close()
    return modified_data


if __name__ == "__main__":
    retrieving_table_data('crypto_project')
