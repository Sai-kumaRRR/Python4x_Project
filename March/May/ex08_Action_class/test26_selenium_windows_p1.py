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


@allure.title("Actions P2")
@allure.description("Verify MouseBack")
def test_verify_action_window():
    # ChromeOptions - --incognio
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(" --incognio")

    driver = webdriver.Chrome(chrome_options)
    driver.get("https://the-internet.herokuapp.com/windows")
    driver.maximize_window()

    parent_window = driver.current_window_handle #1
    print(parent_window) # 104c534ce41d6ab43d3e45yhm

    link = driver.find_element(By.LINK_TEXT, "Click Here")
    link.click()

    window_handles = driver.window_handles #2
    print(window_handles)

    #['56rt87i934dh43276ugtu' , 'd3542t89uy7uui99']

    for handle in window_handles:
        driver.switch_to.window(handle)
        if "New Window" in driver.page_source:
            print("Test cased Passed")
            break

