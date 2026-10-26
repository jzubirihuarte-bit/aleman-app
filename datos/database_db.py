import sqlite3

conn = sqlite3.connect("datos/aleman.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS vocabulario (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    palabra TEXT NOT NULL,

    articulo TEXT,
    plural TEXT,

    espanol TEXT NOT NULL,

    nivel TEXT,
    categoria TEXT,

    tipo_palabra TEXT,

    ejemplo_de TEXT,
    ejemplo_es TEXT,

    aciertos INTEGER DEFAULT 0,
    fallos INTEGER DEFAULT 0,

    dominada INTEGER DEFAULT 0,

    ultima_revision TEXT

)
""")

conn.commit()
conn.close()

print("Base de datos creada")