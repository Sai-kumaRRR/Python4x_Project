import allure
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.devtools.v134.input_ import MouseButton
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains,ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@allure.title("Actions P2")
@allure.description("Verify MouseBack")
def test_verify_action_keyboard():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/pratice.html")

    atag = driver.find_element(By.ID, "click")
    atag.click()

    actions_builders = ActionBuilder(driver=driver)
    actions_builders.pointer_action.pointer_up(MouseButton.BACK)

    time.sleep(10)
    driver.quit()
