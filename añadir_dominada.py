import sqlite3

conn = sqlite3.connect("datos/aleman.db")

cursor = conn.cursor()

cursor.execute("""
ALTER TABLE vocabulario
ADD COLUMN dominada INTEGER DEFAULT 0
""")

conn.commit()
conn.close()

print("dominada añadida")