import allure
from selenium.webdriver.chrome.options import Options
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@allure.title("Alerts")
@allure.description("Verify Alerts")
def test_alerts_confirm():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    # click on the Alert button and check the result - (Assertion of the result)
    # // button[@ onclick = "jsAlert()"]
    # id = "result"
   # element_prompt = driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
    element_confirm = driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")

   # element_prompt.click()
    element_confirm.click()

    WebDriverWait(driver=driver, timeout=5).until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert.dismiss()

    result_text = driver.find_element(By.ID, "result").text

    assert result_text == "You clicked: Cancel"


    time.sleep(5)
