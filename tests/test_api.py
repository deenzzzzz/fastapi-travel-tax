import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from fastapi_travel_tax.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Travel Tax API"}

def test_register():
    response = client.post("/register", json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"
    assert response.json()["is_active"] is True

def test_login():
    client.post("/register", json={"username": "testuser2", "password": "testpass2"})
    response = client.post("/token", data={"username": "testuser2", "password": "testpass2"})
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_get_provinces():
    response = client.get("/provinces")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_tax_reductions():
    response = client.get("/tax-reductions")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_secondary_tax_reductions():
    response = client.get("/tax-reductions/secondary")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
# ...existing code...
