import sqlite3

conexion = sqlite3.connect("profesores.db")
cursor = conexion.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS profes (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, materia TEXT, aura INTEGER)")
conexion.commit()

