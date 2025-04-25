import time
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains,ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@allure.title("JS_03")
@allure.description("Verify JS_03")
def test_js_03():
    #ChromeOptions - --incognito
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(chrome_options)
    driver.get("https://selectorshub.com/xpath-practice-page/")
    driver.maximize_window()
    #Synchronously executes javascript in the current window/frame
    title = driver.execute_script("return document.title")

    # driver.current_url = webdriver finding the url via API request.

    current_url = driver.execute_script("return document.URL")

    print(current_url)
    print(title)

    time.sleep(5)
    driver.quit()



