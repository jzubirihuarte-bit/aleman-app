import sqlite3

conn = sqlite3.connect("datos/aleman.db")
cursor = conn.cursor()

# Sustantivos
cursor.execute("""
UPDATE vocabulario
SET tipo_palabra='Sustantivo'
WHERE articulo IN ('der','die','das')
""")

# Verbos
cursor.execute("""
UPDATE vocabulario
SET tipo_palabra='Verbo'
WHERE categoria='Verbos'
""")

# Adjetivos
cursor.execute("""
UPDATE vocabulario
SET tipo_palabra='Adjetivo'
WHERE categoria='Adjetivos'
""")

# Conectores
cursor.execute("""
UPDATE vocabulario
SET tipo_palabra='Conector'
WHERE categoria='Conectores'
""")

# Expresiones
cursor.execute("""
UPDATE vocabulario
SET tipo_palabra='Expresión'
WHERE categoria='Expresiones'
""")

# Preguntas
cursor.execute("""
UPDATE vocabulario
SET tipo_palabra='Pregunta'
WHERE categoria='Preguntas'
""")

# Adverbios
cursor.execute("""
UPDATE vocabulario
SET tipo_palabra='Adverbio'
WHERE categoria='Adverbios'
""")

conn.commit()
conn.close()

print("Tipo de palabra actualizado")