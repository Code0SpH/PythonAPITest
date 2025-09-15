import requests
from config import BASE_URL

def get_user(user_id):
    return requests.get(f"{BASE_URL}/users/{user_id}")

def create_post(title, body, user_id):
    payload = {"title": title, "body": body, "userId": user_id}
    return requests.post(f"{BASE_URL}/posts", json=payload)