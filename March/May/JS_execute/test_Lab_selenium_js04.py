import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By


@allure.title("JS_03")
@allure.description("Verify JS_03")
def test_js_03():
    # ChromeOptions - --incognito
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(chrome_options)
    driver.get("https://selectorshub.com/xpath-practice-page/")
    driver.maximize_window()

    # scroll into the view where div is present
    username_div = driver.find_element(By.XPATH, "//div[@id='userName']")
    driver.execute_script("arguments[0].scrollIntoView(true);", username_div)

    input_box = driver.execute_script(
        "return document.querySelector('div#userName').shadowRoot.querySelector('#app2').shadowRoot.querySelector('#pizza');")
    input_box.send_keys("farmhouse")

    time.sleep(5)
    driver.quit()

    time.sleep(5)
    driver.quit()
