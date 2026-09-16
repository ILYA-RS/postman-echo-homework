"""Интеграционные тесты: требуют доступа к https://postman-echo.com."""

import requests


BASE_URL = "https://postman-echo.com"
TIMEOUT = 20


def test_get_query_parameters():
    response = requests.get(
        f"{BASE_URL}/get", params={"name": "Alice", "page": "2"}, timeout=TIMEOUT
    )
    assert response.status_code == 200
    assert response.json()["args"] == {"name": "Alice", "page": "2"}


def test_get_custom_header():
    response = requests.get(
        f"{BASE_URL}/get", headers={"X-Homework": "echo-test"}, timeout=TIMEOUT
    )
    assert response.status_code == 200
    assert response.json()["headers"]["x-homework"] == "echo-test"


def test_post_json():
    payload = {"name": "Alice", "age": 25, "active": True}
    response = requests.post(f"{BASE_URL}/post", json=payload, timeout=TIMEOUT)
    assert response.status_code == 200
    body = response.json()
    assert body["json"] == payload
    assert body["headers"]["content-type"].startswith("application/json")


def test_post_form():
    payload = {"name": "Alice", "course": "API testing"}
    response = requests.post(f"{BASE_URL}/post", data=payload, timeout=TIMEOUT)
    assert response.status_code == 200
    body = response.json()
    assert body["form"] == payload
    assert body["headers"]["content-type"].startswith(
        "application/x-www-form-urlencoded"
    )


def test_post_plain_text():
    payload = "Hello, Postman Echo!"
    response = requests.post(
        f"{BASE_URL}/post",
        data=payload,
        headers={"Content-Type": "text/plain"},
        timeout=TIMEOUT,
    )
    assert response.status_code == 200
    body = response.json()
    assert body["data"] == payload
    assert body["headers"]["content-type"].startswith("text/plain")
