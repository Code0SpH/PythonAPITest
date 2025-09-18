import pytest
import requests


@pytest.fixture
def create_user():
    payload = {
        "name": "Fixture Test",
        "email": "fixture@test.com"
    }
    response = requests.post("https://jsonplaceholder.typicode.com/users", json=payload)
    return response.json()

def test_fixture_user(create_user):
    assert create_user["id"] is not None
    assert create_user["name"] == "Fixture Test"
    assert create_user["email"] == "fixture@test.com"


def test_create_post():
    payload = {
        "title": "Test Post",
        "body": "This is a test post",
        "userId": 1
    }
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
    assert response.status_code == 201
    assert response.json()["id"] is not None
    assert response.json()["title"] == "Test Post"


def test_create_comment():
    payload = {
        "name": "Test Comment"
    }
    response = requests.post("https://jsonplaceholder.typicode.com/comments", json=payload)
    assert response.status_code == 201
    assert response.json()["id"] is not None
    assert response.json()["name"] == "Test Comment"