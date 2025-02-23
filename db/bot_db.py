import sqlite3
from db import requests


db = sqlite3.connect('db/store.sqlite3')
cursor = db.cursor()


async def create_tables():
    if db:
        print('база данных подключена')

    cursor.execute(requests.CREATE_TABLE_store)
    cursor.execute(requests.CREATE_TABLE_products_details)



async def sql_insert_store(name_product, size, price,product_id, photo):
    cursor.execute(requests.INSERT_store_query,
                   (name_product, size, price, product_id, photo))
    db.commit()

async def sql_insert_products_details(product_id, category, info_product):
    cursor.execute(requests.INSERT_products_details_query,
                   (product_id, category, info_product))

    db.commit()


def get_db_connection():
    conn = sqlite3.connect('db/store.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn

def fetch_all_products():
    conn = get_db_connection()
    products = conn.execute("""
    select * from store s
    INNER JOIN store_details sd on s.product_id = sd.product_id
    """).fetchall()
    conn.close()
    return products
