import sqlite3

conn = sqlite3.connect("datos/aleman.db")

cursor = conn.cursor()

cursor.execute("""
ALTER TABLE vocabulario
ADD COLUMN tipo_palabra TEXT
""")

conn.commit()
conn.close()

print("tipo_palabra añadida")