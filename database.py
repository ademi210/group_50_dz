# import sqlite3
#
#
# class Database:
#     def __init__(self, path):
#         self.path = path
#
#     def create_tables(self):
#         with sqlite3.connect(self.path) as conn:
#             cursor = conn.cursor()
#             cursor.execute("""
#                 CREATE TABLE IF NOT EXISTS claim(
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     name TEXT,
#                     phone_number TEXT,
#                     text TEXT,
#                     rate INTEGER
#                 )
#             """)
#             conn.commit()
#
#     def add_claim(self, data: dict):
#         print(data)
#         with sqlite3.connect(self.path) as conn:
#             cursor = conn.cursor()
#             cursor.execute(
#                 """
#                 INSERT INTO claim (name, phone_number, text, rate) VALUES (?, ?, ?, ?)
#             """,
#                 (data["name"], data["phone_number"], data["text"], data["rate"]),
#             )
#             conn.commit()
#
#
#
