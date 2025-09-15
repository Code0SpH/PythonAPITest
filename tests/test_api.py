import requests
import pytest

# GET-запросы
def test_get_user():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert "@april.biz" in response.json()["email"]

def test_get_post():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200
    assert response.json()['userId'] == 1
    assert "sunt" in response.json()["title"]

def test_get_comments():
    response = requests.get("https://jsonplaceholder.typicode.com/comments/3")
    assert response.status_code == 200
    assert response.json()['postId'] == 1
    assert "@" in response.json()["email"]

# POST-запросы
def test_create_post():
    payload = {"title": "foo", "body": "bar", "userId": 1}
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
    assert response.status_code == 201
    assert response.json()["title"] == "foo"
    assert response.json()["userId"] == 1

def test_create_albums():
    payload = {"userId": 1, "id": "4", "title": "always title"}
    response = requests.post("https://jsonplaceholder.typicode.com/albums", json=payload)
    assert response.status_code == 201
    assert response.json()["title"] == "always title"
    assert response.json()["userId"] == 1

def test_create_comments():
    payload = {"postId": 101, "id": "501", "name": "always name"}
    response = requests.post("https://jsonplaceholder.typicode.com/comments", json=payload)
    assert response.status_code == 201
    assert response.json()["name"] == "always name"
    assert response.json()["postId"] == 101

# Тест с Параметризацией
@pytest.mark.parametrize("user_id", [1, 2, 3, 4, 5, 6])
def test_get_user_parametrized(user_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["id"] == user_id

@pytest.mark.parametrize("user_id", [1, 2, 3, 4, 5, 6])
def test_get_albums_parametrized(user_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["id"] == user_id

@pytest.mark.parametrize("id", [1, 2, 3, 4, 5, 6])
def test_get_photos_parametrized(id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/photos/{id}")
    assert response.status_code == 200
    assert response.json()["id"] == id


