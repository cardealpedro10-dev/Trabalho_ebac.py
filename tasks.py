import math
from celery import Celery

# Criação da instância do Celery
app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def soma(a, b):
    """Soma dois números recebidos."""
    return a + b

@app.task
def fatorial(n):
    """Calcula o fatorial de um número inteiro não negativo."""
    if n < 0:
        raise ValueError("O número deve ser maior ou igual a zero.")
    return math.factorial(n)

 
