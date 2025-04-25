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

class TestSelenium:

    def __init__(self):
        self.driver = None

    def open_browser(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--incognito")

        self.driver = webdriver.Chrome(self.chrome_options)
        self.driver.get("https://selectorshub.com/xpath-practice-page/")
        self.driver.maximize_window()



@allure.title("JS_03")
@allure.description("Verify JS_03")
def test_js_03(self):
    title = self.driver.execute_script("return document.title")
    current_url = self.driver.execute_script("return document.URL")
    print(current_url)
    print(title)


def close_browser(self):
        time.sleep(3) # wait for 3 seconds before closing
        self.driver.quit()



