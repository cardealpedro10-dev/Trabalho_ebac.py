# Testes Unitários para Tasks do Celery com Pytest

Este repositório contém a solução do exercício do **Módulo 32** do curso da EBAC, focado em testes unitários para tarefas assíncronas do Celery utilizando o framework **Pytest**.

## 📌 Sobre o Projeto

As tarefas assíncronas processadas pelo Celery frequentemente contêm regras de negócio essenciais em aplicações backend. Testar essas funções diretamente garante que a lógica de negócio esteja correta e livre de regressões, sem a necessidade de manter *workers* do Celery ou corretores de mensagens (*brokers*) em execução durante os testes.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Celery** (Processamento de tarefas assíncronas)
* **Pytest** (Framework de testes unitários)

---

## 📂 Estrutura do Projeto


 
Trabalho_ebac.py/
├── tasks.py        # Código das tarefas Celery (soma e fatorial)
├── test_tasks.py   # Testes unitários com Pytest
└── README.md       # Documentação do projeto

 # Como executar o projeto

 # 1 intalações das dependencias

 pip intall celery pytest 

 # Executando os testes automatizados.

 ptython -m pytest -v test_task_tasks.py

 # Resultados finais dos testes.

 test_tasks.py::test_soma_sucesso PASSED                                 [ 20%]
test_tasks.py::test_soma_numeros_negativos PASSED                       [ 40%]
test_tasks.py::test_fatorial_numero_positivo PASSED                     [ 60%]
test_tasks.py::test_fatorial_caso_de_borda_zero PASSED                  [ 80%]
test_tasks.py::test_fatorial_caso_de_borda_um PASSED                    [100%]

============================== 5 passed in 0.59s ==============================

 