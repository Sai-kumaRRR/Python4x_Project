import allure
from selenium.webdriver.chrome.options import Options
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui  import Select

@allure.title("SVG")
@allure.description("Verify SVG")
def test_alerts_js_Alert():
    driver = webdriver.Chrome()
    driver.get("https://www.filpkart.com/")


    search_box = driver.find_element(By.ID, "q")
    search_box.send_keys("macmini")


    list_svg_elements = driver.find_elements(By.XPATH, "//*[name()='svg']")
    list_svg_elements[0].click()


time.sleep(5)