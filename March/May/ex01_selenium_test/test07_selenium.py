import allure
import pytest
from selenium import webdriver
import time


@allure.title("Verify that the title of vwo.com is executed.")
def test_katalon_chrome():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    time.sleep(10)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"



def test_katalon_edge():
    driver = webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    time.sleep(20)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"



def test_katalon_firefox():
    driver = webdriver.Firefox()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    time.sleep(30)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"