import time

import allure
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


@allure.title("Exception")
@allure.description("Verify Exception_handle")
def test_alerts_verify_Exception_Handle():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    try:
        element = driver.find_element(By.ID, "this_id_does'nt_exist")
    except NoSuchElementException as nse:
        print(nse.msg)

    time.sleep(5)
