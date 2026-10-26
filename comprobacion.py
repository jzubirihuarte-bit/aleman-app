import sqlite3
import pandas as pd

conn = sqlite3.connect("datos/aleman.db")

df = pd.read_sql("""
SELECT nivel, COUNT(*) AS cantidad
FROM vocabulario
GROUP BY nivel
""", conn)

print(df)

conn.close()