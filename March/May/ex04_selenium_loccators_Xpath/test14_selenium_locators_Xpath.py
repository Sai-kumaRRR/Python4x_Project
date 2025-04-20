import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@allure.title("VWO Login Negative TestCase")
@allure.description("TC1- Negative TC - VWO Login with invalid creds")
@pytest.mark.negtivevwologin
def test_app_vwo_login_chrome():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_app_btn = driver.find_element(By.XPATH, "//a[contains(text(),'Make')")
    make_app_btn.click()

    # text() - EXACT Match

    # pratial Text() - contains()

    # //a[contains(text(),'make Appointment')]
    # //a[contains(text(),' Appointment')]
    # //a[contains(text(),'make')]
    # //a[contains(text(),'ma')]
    # //a[contains(text(),'App')] - this my fail if there 1 or more a tag with app
    # //<a rel = "https:/google.com"/>
    # a//[starts-with(text(),'make')]



    time.sleep(5)
    driver.quit()  # close every thing.
