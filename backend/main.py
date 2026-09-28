from manager import Manager 
from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware as mw
from modelos import docente

control = Manager()

app = FastAPI()

app.add_middleware(
    mw,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.get("/listar")
def getProfe(profe: docente):
    control.listarProfe(profe)

@app.post("/agregar")
def postProfe(profe: docente):
  control.agregarProfe(profe)

@app.put("/editar")
def putProfe(profe: docente):
    control.editarProfe(profe)

@app.delete("/eliminar")
def deleteProfe(idProfe: int):
    control.eliminarProfe(idProfe)
