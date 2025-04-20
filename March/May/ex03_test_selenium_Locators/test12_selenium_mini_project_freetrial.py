import os
import time

import allure
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@allure.title("VWO Login Negative TestCase")
@allure.description("TC1- Negative TC - VWO Login with invalid creds")
@pytest.mark.negtivevwologin
def test_app_vwo_login_chrome():
    load_dotenv()
    chrome_options = Options()
    chrome_options.add_argument(" --incognito")
    driver = webdriver.Chrome(chrome_options)
    driver.get(os.getenv("URL"))

    # <a
    # href = "https://vwo.com/free-trial/?utm_medium=website&amp;utm_source=login-page"
    # class ="text-link"
    # data-qa = "bericafeqo"
    # start a free trial
    # </a>

    # LinkText and Partial text

    # LINK_TEXT = EXACT_MATCH
    anchor_tag_element = driver.find_element(By.LINK_TEXT, "Start a free trial")
    anchor_tag_element.click()

    # PARTIAL_LINK_TEXT - contains
    anchor_tag_element = driver.find_element(By.PARTIAL_LINK_TEXT, "free trial")
    anchor_tag_element.click()


webdriver.current_url == "https://vwo.com/free-trial/?utm_medium=website&utm_source=link"

    time.sleep(5)
    driver.quit()  # close something.
