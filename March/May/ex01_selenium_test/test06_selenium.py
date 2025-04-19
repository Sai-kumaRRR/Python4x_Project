import allure
import pytest
from selenium import webdriver


@allure.title("Verify that the title of vwo.com is executed.")
def test_vwo_sample():
    driver = webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    if"PURA Healthcare Service" in driver.page_source:
        print("Text Found!!, Test case Passed!")
    else:
        print("Text not found on the page")
        pytest.fail("Text not found on the page")

          # close the browser / py Int - is closing