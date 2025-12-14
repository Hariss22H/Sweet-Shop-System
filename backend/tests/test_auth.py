from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_user_registration():
    response = client.post(
        "/api/auth/register",
        json={
            "username": "testuser",
            "password": "testpassword"
        }
    )
    assert response.status_code == 201
    assert response.json()["message"] == "User registered successfully"


def test_user_login():
    response = client.post(
        "/api/auth/login",
        json={
            "username": "testuser",
            "password": "testpassword"
        }
    )

    assert response.status_code == 200
    assert "access_token" in response.json()
