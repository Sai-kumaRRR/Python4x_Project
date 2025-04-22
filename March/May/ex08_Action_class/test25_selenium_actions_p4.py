from selenium import webdriver
import time
import allure
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.devtools.v134.input_ import MouseButton
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains,ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@allure.title("Make My Trip Automation")
@allure.description("Verify Make Trip Automation by using Action Classes")
def test_verify_action_makemytrip():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(" --incognito")