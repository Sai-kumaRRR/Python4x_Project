import pytest
import allure
import requests


@allure.title("verify the GET Request of restful booker")
@allure.description("This Testcase check booking 1 and verify the response")
@pytest.mark.positive
def test_get_request_positive():
    URL ="https://restful-booker.herokuapp.com/booking/1"
    response_data =requests.get(url=URL)
    assert response_data.status_code ==200
