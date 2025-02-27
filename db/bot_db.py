import sqlite3
from db import requests


db = 'db/store.sqlite3'


async def create_tables():
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    if db:
        print('База данных подключена')

    cursor.execute(requests.CREATE_TABLE_store)
    cursor.execute(requests.CREATE_TABLE_products_details)
    cursor.execute(requests.CREATE_TABLE_collection_products)

    conn.commit()
    conn.close()


async def sql_insert_store(name_product, size, price,product_id, photo):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(requests.INSERT_store_query,
                       (name_product, size, price, product_id, photo))

    conn.commit()
    conn.close()


async def sql_insert_products_details(product_id, category, info_product):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(requests.INSERT_products_details_query,
                       (product_id, category, info_product))

    conn.commit()

async def sql_insert_collection_products(product_id, collection):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(requests.INSERT_collection_products_query,
                       (product_id, collection))

    conn.commit()
    conn.close()




def get_db_connection():
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    return conn


def fetch_all_products():
    conn = get_db_connection()
    cursor = conn.cursor()
    products = cursor.execute("""
    select * from store s
    INNER JOIN collection_products cp on s.product_id = cp.product_id
    """).fetchall()
    conn.commit()
    conn.close()
    return products

def update_product_field(product_id, field_name, new_value):
    conn = get_db_connection()

    store_table = ['name_product', 'price', 'size', 'product_id', 'photo']
    store_details_table = ['category', 'product_id']


    try:
        if field_name in store_table:
            query = f'UPDATE store SET {field_name} = ? WHERE product_id = ?'
        elif field_name in store_details_table:
            query = f'UPDATE store_details SET {field_name} = ? WHERE product_id = ?'

        else:
            raise ValueError(f'Нет такого поля как {field_name}')

        conn.execute(query, (new_value, product_id))
        conn.commit()

    except sqlite3.OperationalError as error:
        print(f'Ошибка - {error}')

    finally:
        conn.close()
