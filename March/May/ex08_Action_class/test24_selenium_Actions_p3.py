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


@allure.title("Actions P3")
@allure.description("Verify click and hold")
def test_verify_action_keyboard():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    #draggable
    element_to_hold = driver.find_element(By.ID, "draggable")

    #KEY_DOWN
    actions = ActionChains(driver)
    actions.click_and_hold(on_element=element_to_hold).perform()

    time.sleep(10)
    driver.quit()

