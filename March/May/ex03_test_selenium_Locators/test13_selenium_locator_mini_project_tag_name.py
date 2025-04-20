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
    all_links_page = driver.find_elements(By.TAG_NAME, "a")
    print(len(all_links_page))
    for i in all_links_page:
        print(i.text)
        if "Strat a free trial" in i.text:
            i.click()

    time.sleep(5)
    driver.quit()  # close every thing.
