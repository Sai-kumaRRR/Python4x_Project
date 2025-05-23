import time

import allure
from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


@allure.title("Stale_element")
@allure.description("stale_element")
def test_stale_element__exception_demo():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    try:
        textarea = driver.find_element(By.NAME, "q")
        driver.refresh()
        #{ 'status' 404, 'value': {"error": stale element reference"}
        textarea.send_keys("The Testing Academy")
    except StaleElementReferenceException as see:
        # stale element reference

        print(see)
        print("Stale element reference" )

        time.sleep(5)