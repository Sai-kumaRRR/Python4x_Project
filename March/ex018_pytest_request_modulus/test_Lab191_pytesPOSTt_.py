import pytest
import allure
import requests


#pip install allure report

# to make request

@allure.title("TC#1 - create booking CRUD positive")
@allure.description("verify the create booking")
@pytest.mark.crud
def test_create_booking_positive_tc1():
    base_url = "https://restful-booker.herokuapp.com"
    base_path_post = "/booking"
    # base_path_put ="/booking/1"


    full_url = base_url + base_path_post
    headers ={
        "Content-Type" : "application/json"

    }
    payload ={

    }













@allure.title("TC#1 - create booking CRUD positive")
@allure.description("verify the create booking")
@pytest.mark.crud
def test_create_booking_positive_tc1():