import time
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.devtools.v134.input_ import MouseButton
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains,ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton


@allure.title("Actions P3")
@allure.description("Verify click and hold")
def test_verify_action_windows():
     # ChromeOptions = --incognito
     chrome_options = webdriver.chromeOptions()
     chrome_options.add_argument("--incognito")

     driver = webdriver.Chrome(chrome_options)
     driver.get("https://app.vwo.com/#/test/ab/13/heatmap/1?token=eyJhY2NvdW50X2")
     driver.maximize_window()

     main_window_handle = driver.current_window_handle # 1
     list = driver.find_elements(By.CSS_SELECTOR, "[data-qa='yedexafobi']")
     # control = 0
     # version = 1

     variation = list[1]

     actions = ActionChains(driver)
     actions.click(variation).perform()


     time.sleep(15)

     all_handles = driver.window_handles  # 2
