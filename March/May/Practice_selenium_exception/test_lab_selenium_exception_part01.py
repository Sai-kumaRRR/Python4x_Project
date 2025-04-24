import allure
from selenium.webdriver.chrome.options import Options
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui  import Select

@allure.title("Exception")
@allure.description("Verify Exception")
def test_alerts_verify_Exception():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    element = driver.find_element(By.ID, "this_id_does'nt_exist")

    #response =
    # {'status': 404, 'value':

    #{"value" : {"no such element", "message":

    #" no such element: untable to locate element

    # No Such elementException

    time.sleep(5)