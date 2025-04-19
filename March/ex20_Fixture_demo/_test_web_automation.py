import allure # pip install allure
import pytest # pip install pytest
import requests # pip install requests



def test_selenium(launch_browser, close_browser):
    launch_browser
    print("DO Tc")
    close_browser
