from database import conexion, cursor
from modelos import docente

class Manager:
    def __init__(self):
        pass

    def listarProfe(self, profesor: docente):
        cursor.execute("SELECT * FROM profes (nombre, materia, aura) WHERE nombre = ?", (profesor.nombre))

    def agregarProfe(self, profesor: docente):
        cursor.execute("INSERT INTO profes (nombre, materia, aura) VALUES (?, ?, ?)", (profesor.nombre, profesor.materia, profesor.aura))
        conexion.commit()

    def editarProfe(self, profesor: docente):
        cursor.execute("UPDATE profes SET nombre = ?, materia = ?, aura = ?", (profesor.nombre, profesor.materia, profesor.aura))
        conexion.commit()

    def eliminarProfe(self, profesor: int):
        conexion.execute("DELETE FROM profes WHERE id = ?", (profesor,))
