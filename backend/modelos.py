from pydantic import BaseModel

class docente(BaseModel):
    nombre: str
    materia: str
    aura: int
