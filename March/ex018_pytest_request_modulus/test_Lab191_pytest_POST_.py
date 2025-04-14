import pytest
import allure
import requests


#pip install allure report

# to make request

# https://jsonpathfinder.com
#x.booking.booking dates.checkin
#response_data_json["booking"]["booking dates"]["checkin"]

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
        "firstname": "Jim",
        "lastname" : "Brown",
        "total price": 111,
        "deposit paid": True ,
        "booking dates":{
            "checkin":"2018-01-01",
            "checkout":"2019-01-01"
        },
        "additional needs":"Breakfast"

    }
    response_data = requests.post(url=full_url,headers=headers, json=payload)

    #Status.code verification
    assert response_data.status_code == 200

    #booking ID> 0, firstname ==Jim
    response_data_json = response_data.json()
    bookingid = response_data_json["bookingid"]
    print(bookingid)
    assert bookingid is not None
    assert bookingid > 0
    assert type(bookingid) == int

    firstname = response_data_json["booking"]["firstname"]
    assert firstname == "Jim"
    assert type(firstname) == str

    lastname = response_data_json["booking"]["lastname"]
    totalprice = response_data_json["booking"]["total price"]
    depositpaid  =response_data_json["booking"]["depositpaid"]


    assert lastname =="Brown"
    assert totalprice ==111
    assert depositpaid == True

    checkin = response_data_json["booking"]["booking dates"]["checkin"]
    checkout = response_data_json["booking"]["booking dates"]["checkout"]
    assert checkin == "2018-01-01"
    assert checkout == "2018-01-01"


    time = response_data.elapsed.total_seconds()
    assert time < 3



@allure.title("TC#2 - create booking CRUD negative")
@allure.description("verify the invalid payload booking is not created!")
@pytest.mark.crud
def test_create_booking_negative_tc1():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    json_payload ={}
    response = requests.post(url = URL, headers = headers, json = json_payload)
    assert response.status_code == 500
    assert response.text == "Internal Server Error"


