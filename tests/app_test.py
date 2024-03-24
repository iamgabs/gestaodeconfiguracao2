import os
import sys
import pytest 
from src.app import app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture
def client() -> object:
    with app.test_client() as client:
        yield client


def test_get_products(client) -> None: 
    """
    Testing if the answer is "ok" 
    is a list of products 
    and the list is not empty 
    """
    response:object = client.get("/products")
    assert response.status_code == 200
    assert response.is_json
    data:object = response.get_json()
    assert type(data) == list  
    assert len(data) > 0  


def test_create_product(client) -> None :
    """
    Testing if the answer is "created" 
    is a list of the product 
    """
    new_product = {
        "name": "Orange",
        "price": 1.50,
        "amount": 500
    }
    response = client.post("/new_product", json=new_product)
    assert response.status_code == 201
    assert response.is_json
    data = response.get_json()
    assert data['name'] == new_product['name']
    assert data['price'] == new_product['price']
    assert data['amount'] == new_product['amount']
