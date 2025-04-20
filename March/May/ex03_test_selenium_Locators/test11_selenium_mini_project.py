from selenium import webdriver
import allure
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from dotenv import load_dotenv
import os

@allure.title("VWO Login Negative TestCase")
@allure.description("TC1- Negative TC - VWO Login with invalid creds")
@pytest.mark.negtivevwologin
def test_app_vwo_login_chrome():
    load_dotenv()
    chrome_options = Options()
    chrome_options.add_argument(" --incognito")
    driver = webdriver.Chrome(chrome_options)
    driver.get(os.getenv("URL"))

# 1. - find the email and enter the wrong username or email
    # <input
    # type="email"

    # class = "text-input w(100%)
    # name = "username"
    # id = "login-username"
    #data-qa="hocewoqisi"
    #>
    email_web_element = driver.find_element(By.ID, "login-username")
    email_web_element.send_keys(os.getenv("INVALID_USERNAME"))

    #<input
    # type-"password"
    #class="text-input w(100%)
    #name ="password"
    #id="login-password"
    #data-qa="jobodapuxe"
    #data-gtm-from-interact-field-id="i">

    password_web_element = driver.find_element(By.NAME,"password")
    password_web_element.send_keys(os.getenv("INVALID_PASSWORD"))

    #<button
    # type = "sumit"
    # id = "js-login-btn"
    # class="btn btn--positive btn--inverted w(100%) H(48px) fz(16px)'
    #onclick="login.login(event)"
    #data-qa="sibequkica">


    sumit_btn_web_element = driver.find_element(By.ID,"js-login-btn")
    sumit_btn_web_element.click()

# wait for sometime
    time.sleep(3)

    #< dir
    # class="notification-box-description"
    # id="js-notification-box-msg"
    #data-qa="rixawilomi">
    #your email, password , IP address or location did not match
    # </div>

    error_message_web_element = driver.find_element(By.ID, "js-notification-box-msg")
    print(error_message_web_element.text)

    assert error_message_web_element.text == os.getenv("error_message_expected")

    time.sleep(5)
    driver.quit() # close everything.