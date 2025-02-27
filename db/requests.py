CREATE_TABLE_store = """
    CREATE TABLE IF NOT EXISTS store (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_product TEXT,
    size TEXT,
    price FLOAT,
    photo TEXT,
    product_id TEXT
    )
"""

CREATE_TABLE_products_details = """
    CREATE TABLE IF NOT EXISTS products_details(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id TEXT,
    category TEXT,
    info_product TEXT
    )
"""


CREATE_TABLE_collection_products = """
    CREATE TABLE IF NOT EXISTS collection_products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id TEXT,
    collection TEXT,
    FOREIGN KEY (product_id) REFERENCES store (product_id) ON DELETE CASCADE
    )
"""


INSERT_store_query = """
    INSERT INTO store (name_product, size, price, photo, product_id)
    VALUES (?,?,?,?,?) 
"""

INSERT_products_details_query = """
    INSERT INTO products_details (product_id, category, info_product)
    VALUES (?,?,?)
"""

INSERT_collection_products_query = """
    INSERT INTO collection_products (product_id, collection)
    VALUES (?, ?)
"""