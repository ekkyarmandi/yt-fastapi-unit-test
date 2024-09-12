import sys
import os

sys.path.append(os.getcwd())

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_hello():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_operator_tambah():
    response = client.get("/tambah?a=1&b=2")
    assert response.status_code == 200
    assert response.json() == {"result": 3}


def test_operator_tambah_error():
    try:
        client.get("/tambah?a=-1&b=-2")
    except ValueError as e:
        assert str(e) == "a dan b harus positif"


def test_operator_pengurangan():
    response = client.get("/pengurangan?a=2&b=1")
    assert response.status_code == 200
    assert response.json() == {"result": 1}
