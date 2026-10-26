import sqlite3
import pandas as pd

conn = sqlite3.connect("datos/aleman.db")

df = pd.read_sql("""
SELECT tipo_palabra,
COUNT(*) cantidad
FROM vocabulario
GROUP BY tipo_palabra
""", conn)

print(df)

conn.close()