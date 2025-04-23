import time
import pytest
from selenium.webdriver.support.ui import Select
import allure
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@allure.title("Make My Trip Automation")
@allure.description("Verify Make Trip Automation by using Action Classes")
def test_verify_action_makemytrip():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(" --incognito")

    driver = webdriver.Chrome(chrome_options)
    driver.get("https://www.makemytrip.com/")
    driver.maximize_window()

    WebDriverWait(driver=driver, timeout=5).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@data-cy='closeModel']"))

    )
    driver.find_element(By.XPATH, "//span[@data-cy='closeModel']").click()

    time.sleep(2)

    formCity = driver.find_element(By.ID, "fromCity")

    actions = ActionChains(driver=driver)
    actions.move_to_element(formCity).click().send_keys("del").perform()

    time.sleep(2)

    actions.move_to_element(formCity).key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()

    time.sleep(10)
    driver.quit()
