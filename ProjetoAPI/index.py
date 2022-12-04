from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, Union
from datetime import date


app = FastAPI()

class Fila(BaseModel):
    id: Optional [int] = 0
    nome: str = Field (max_length=20)
    prioridade: str = Field (maenx_length=1)
    posicao:Optional [int] = 0
    data: Optional[date] = '2022-12-04'
    atendido: Optional [bool] = False

repositorioFila = [
    Fila(id=1,nome="Nayara",prioridade="N",posicao=1,data='2022-12-04',atendido=False), 
    Fila(id=2,nome="Gabriel",prioridade="N",posicao=2,data='2022-12-04',atendido=False), 
    Fila(id=3,nome="Victor",prioridade="P",posicao=3,data='2022-12-04',atendido=False), 
    Fila(id=4,nome="Igor",prioridade="N",posicao=4,data='2022-12-04',atendido=False),
    Fila(id=5,nome="Sebastian",prioridade="P",posicao=5,data='2022-12-04',atendido=False), 
    Fila(id=6,nome="Lucas",prioridade="P",posicao=6,data='2022-12-04',atendido=False),
    Fila(id=7,nome="Daniela",prioridade="N",posicao=7,data='2022-12-04',atendido=False) 
]


    

@app.get("/fila")
def listar():
    return {"Fila": repositorioFila}
 
@app.get("/fila/{id}")
def posicao_cliente(id:int):
    if [fila for fila in repositorioFila if fila.id==id] == []:
        raise HTTPException(status_code=404, detail="Posição Vazia ")
    return{"Fila": [fila for fila in repositorioFila if fila.id==id]}

@app.post("/fila/")
async def criar_fila(fila: Fila):
    if fila.prioridade == 'N'  or  fila.prioridade == 'P':
        fila.id = repositorioFila[-1].id + 1
        fila.posicao = repositorioFila[-1].id + 1
        fila.atendido = False
        fila.data = date.today()
        repositorioFila.append(fila)
    else:
        raise HTTPException(status_code=404, detail="Verifique a Preferencia digitada")



@app.patch("/fila/{id}/")
def update_fila(id:int, fila:Fila):
    index = [index for index, fila in enumerate(repositorioFila) if fila.id == id]
    if fila.atendido == True:
        fila.posicao = 0
        fila.data = date.today()
    fila.id = repositorioFila[index[0]].id
    repositorioFila[index[0]] = fila
    return{"mensagem" : "Alteração efetuada"}

@app.delete("/fila/{id}")
def deletar_fila(id:int):
    fila = [fila for fila in repositorioFila if fila.id ==id]
    repositorioFila.remove(fila[0])
    return()










