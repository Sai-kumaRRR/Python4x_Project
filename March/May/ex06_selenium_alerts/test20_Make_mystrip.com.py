import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@allure.title("Alerts")
@allure.description("Verify Alerts")
def test_alerts_js_alert_normal():
    driver = webdriver.Chrome()
    driver.get("https://www.makemytrip.com/")

    WebDriverWait(driver=driver, timeout=3).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter Mobile Number']")))

    modal = driver.find_element(By.XPATH, "//input[@placeholder='Enter Mobile Number']")
    modal.send_keys("987654321")

    continue_button = driver.find_element(By.XPATH, "//span[normalize-space()='Continue']")
    continue_button.click()


