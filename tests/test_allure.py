import requests
import pytest
import allure


@allure.title("Test Get User")
@allure.description("Проверка получения пользователя по ID")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_user():
    with allure.step("Отправка запроса"):
        response = requests.get("https://jsonplaceholder.typicode.com/users/1")

    with allure.step("Проверка статуса"):
        assert response.status_code == 200

    with allure.step("Проверка данных пользователя"):
        user_data = response.json()
        assert user_data["id"] == 1
        assert user_data["name"] == "Leanne Graham"
        assert "@april.biz" in user_data["email"]