import math
import time
from celery import Celery

# Configuração do Celery com Redis como broker e backend
celery_app = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
)


@celery_app.task
def calcular_soma(a: float, b: float) -> float:
    """Simula um processamento demorado e retorna a soma de dois números."""
    time.sleep(5)
    return a + b


@celery_app.task
def calcular_fatorial(n: int) -> int:
    """Calcula o fatorial de forma eficiente e simula processamento demorado."""
    if n < 0:
        raise ValueError("Fatorial não é definido para números negativos.")
    time.sleep(5)
    return math.factorial(n)

 
