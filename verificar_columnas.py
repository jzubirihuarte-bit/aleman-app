import sqlite3

conn = sqlite3.connect("datos/aleman.db")

cursor = conn.cursor()

cursor.execute("""
PRAGMA table_info(vocabulario)
""")

for row in cursor.fetchall():
    print(row)

conn.close()