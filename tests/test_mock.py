import requests



def test_mocked_api_with_pytest_mock(mocker):
    mock_response_data = {
        "id": 1,
        "name": "Mocked User",
        "email": "mock@example.com"
    }

    mock_response = mocker.Mock()
    mock_response.json.return_value = mock_response_data
    mock_response.status_code = 200

    mocker.patch('requests.get', return_value=mock_response)

    response = requests.get("https://jsonplaceholder.typicode.com/users/1")

    assert response.status_code == 200
    assert response.json() == mock_response_data

def test_mocked_response_status():
    for status_code in [200, 404, 500]:
        response = requests.get(f"https://httpbin.org/status/{status_code}")
        assert response.status_code == status_code

def test_mocked_response_headers():
    response = requests.get("https://httpbin.org/headers")
    assert "headers" in response.json()
    assert "User-Agent" in response.json()["headers"]