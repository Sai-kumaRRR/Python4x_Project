import allure
import pytest
from selenium import webdriver


@allure.title("Open the app.vwo.com")
@pytest.mark.regression
def test_vwo_login():
    driver = webdriver.Chrome()


     # 1) This code is translated into the API request
     # 2) post request - browser driver(server)
     # 3) where it will create a session or fresh copy browser
     # 4)session id - 16 digit (dasasdctgrg) will be created

    driver.get("https://app.vwo.com")
    print(driver.session_id)

# 5)GET -> GET API request to nevigate to praticular page
# 6)  browser will navigate to the URL

# source code (client) -> API Request(w3c) -> browser driver (server)-> browser
