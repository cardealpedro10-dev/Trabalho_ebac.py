import pytest
from tasks import soma, fatorial  # Importa as funções diretamente do arquivo tasks.py


# --- Testes para a Task de Soma ---
def test_soma_sucesso():
    """Valida se a task de soma calcula corretamente o resultado de dois números."""
    resultado = soma(5, 3)
    assert resultado == 8, "A soma de 5 + 3 deve ser igual a 8"


def test_soma_numeros_negativos():
    """Valida a soma envolvendo números negativos."""
    resultado = soma(-1, -4)
    assert resultado == -5, "A soma de -1 + -4 deve ser igual a -5"


# --- Testes para a Task de Fatorial ---
def test_fatorial_numero_positivo():
    """Valida o cálculo do fatorial de um número inteiro positivo."""
    resultado = fatorial(5)
    assert resultado == 120, "O fatorial de 5 deve ser 120"


def test_fatorial_caso_de_borda_zero():
    """Valida o caso de borda obrigatório: o fatorial de 0 deve ser igual a 1."""
    resultado = fatorial(0)
    assert resultado == 1, "O fatorial de 0 deve ser igual a 1"


def test_fatorial_caso_de_borda_um():
    """Valida o caso de borda do fatorial de 1, que deve retornar 1."""
    resultado = fatorial(1)
    assert resultado == 1, "O fatorial de 1 deve ser igual a 1"

 
