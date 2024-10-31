import pytest
from src.models.sqlite.settings.connection import SqliteConnectionHandle
from .products_repository import ProductRepository

conn_handle = SqliteConnectionHandle()
conn = conn_handle.connect()

# Testes de Integração com o Banco de Dados.
@pytest.mark.skip(reason="interacao com o banco")
def test_insert_product():
    repo = ProductRepository(conn)

    name = "algumaCoisa2"
    price = 12.34
    quantity = 8

    repo.insert_product(name, price, quantity)
    print(repo)

@pytest.mark.skip(reason="interacao com o banco")
def test_find_product():
    repo = ProductRepository(conn)

    name = "algumaCoisa2"
    response = repo.find_product_by_name(name)
    print(response)
    print(type(response))
