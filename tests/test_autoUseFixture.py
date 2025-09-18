import pytest
import requests

# Определяем фикстуру base_url
@pytest.fixture(scope="session")
def base_url():
    return "https://jsonplaceholder.typicode.com"

# Определяем фикстуру user, которая использует base_url
@pytest.fixture
def user(base_url):
    response = requests.get(f"{base_url}/users/1")
    return response.json()

# Фикстура setup теперь может использовать base_url
@pytest.fixture(autouse=True)
def setup(base_url):
    print(f"\nRunning tests against {base_url}")

def test_user_name(user):
    assert user["name"] == "Leanne Graham"

def test_user_email(user):
    assert user["email"] == "Sincere@april.biz"

def test_user_username(user):
    assert user["username"] == "Bret"

def test_user_phone(user):
    assert user["phone"] == "1-770-736-8031 x56442"