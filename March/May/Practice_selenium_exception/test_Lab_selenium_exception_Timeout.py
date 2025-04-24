import time

import allure
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,NoSuchElementException


@allure.title("Timeout")
@allure.description("Timeout")
def test_stale_element_exception_demo():
    driver = webdriver.Chrome()
    driver.get("https://google.com")

    driver.get("https://google.com")
    try:
        WebDriverWait(driver=driver, timeout=10).until(EC.element_to_be_clickable((By.ID, "submit")))
        print("End of the program")
    except TimeoutException as see:
        #stale element reference
        print(see)
        print("TimeoutException occured!:, 10seconds Passed")
    finally:
        driver.quit()
