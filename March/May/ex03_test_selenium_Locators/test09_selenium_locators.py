from selenium import webdriver
import allure
import pytest
import time
from selenium.webdriver.common.by import By


def test_katalon_firefox():
    driver = webdriver.Firefox()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

# 1. - find the element the anchor tag
    # <a
    # id = "btn-make-appointment"
    # href="./profile.ph#login"
    # class="btn btn-dark btn-lg">
    # make Appointment
    # </a>
    make_appointment_element = driver.find_element(By.ID, "btn-make-appointment")

    # 2. click on it
    make_appointment_element.click()

    # 4. - verify that URL changes
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    time.sleep(10)
    driver.quit()  # close everything.
