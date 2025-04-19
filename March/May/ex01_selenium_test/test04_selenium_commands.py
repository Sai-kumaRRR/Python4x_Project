import allure
import pytest
from selenium import webdriver


@allure.title("Verify that the title of vwo.com is executed.")
def test_vwo_sample():
    driver = webdriver.Edge()
    driver.get("https://app.vwo.com")
    print(driver.title)
    assert driver.title == "Login - VWO"
