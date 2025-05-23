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


@allure.title("JS")
@allure.description("Verify JS")
def test_js():

    #ChromeOptions - --incognito
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(chrome_options)
    driver.get("https://app.vwo.com")
    driver.maximize_window()

    #Synchronously executes javascript in the current window/frame
    driver.execute_script("alert(1)")

    time.sleep(5)
    driver.quit()



