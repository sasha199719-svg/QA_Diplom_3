import pytest
import requests

from selenium import webdriver

from data import BASE_URL, REGISTER_ENDPOINT, DELETE_USER_ENDPOINT
from helpers import generate_user


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        browser = webdriver.Chrome()
    else:
        browser = webdriver.Firefox()

    browser.maximize_window()

    yield browser

    browser.quit()


@pytest.fixture
def user():
    user_data = generate_user()

    response = requests.post(
        BASE_URL + REGISTER_ENDPOINT,
        json=user_data
    )

    access_token = response.json().get("accessToken")

    yield user_data

    if access_token:
        requests.delete(
            BASE_URL + DELETE_USER_ENDPOINT,
            headers={
                "Authorization": access_token
            }
        )