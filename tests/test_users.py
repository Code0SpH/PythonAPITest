import pytest
from utils.helpers import get_user, create_post
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def test_get_user():
    response = get_user(1)
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert "@april.biz" in response.json()["email"]

@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_user_parametrized(user_id):
    response = get_user(user_id)
    assert response.status_code == 200
    assert response.json()["id"] == user_id

