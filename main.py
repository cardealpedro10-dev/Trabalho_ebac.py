from celery_app import calcular_fatorial, calcular_soma
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="API de Tarefas Assíncronas com Celery")


class SomaRequest(BaseModel):
    a: float
    b: float


class FatorialRequest(BaseModel):
    n: int


@app.post("/soma")
def endpoint_calcular_soma(payload: SomaRequest):
    task = calcular_soma.delay(payload.a, payload.b)
    return {
        "mensagem": "Tarefa de soma enviada com sucesso!",
        "task_id": task.id,
        "status": "PROCESSANDO",
    }


@app.post("/fatorial")
def endpoint_calcular_fatorial(payload: FatorialRequest):
    if payload.n < 0:
        raise HTTPException(
            status_code=400,
            detail="O número para fatorial deve ser maior ou igual a zero.",
        )
    task = calcular_fatorial.delay(payload.n)
    return {
        "mensagem": "Tarefa de fatorial enviada com sucesso!",
        "task_id": task.id,
        "status": "PROCESSANDO",
    }

 
