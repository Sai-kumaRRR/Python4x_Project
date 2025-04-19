import time

import allure
import pytest
from selenium import webdriver


@allure.title("Open the app.vwo.com")
@pytest.mark.regression
def test_vwo_login():
    driver = webdriver.Edge()
    driver.get("https://app.vwo.com")
    time.sleep(15)
