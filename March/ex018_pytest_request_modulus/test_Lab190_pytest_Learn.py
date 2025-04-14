import allure
import pytest


# pip install pytest allure requests

@allure.title("TC#1 - verify that 2-2 =0")
@allure.description("This is a basic math test")
@pytest.mark.smoke
def test_basic_math():
    assert 2 - 2 == 0


@allure.title("TC#2 - verify that 3 - 3 is equal to 0")
@allure.description("this is a smoke testcase which check verify that 3 - 3 is equal")
@pytest.mark.regression
def test_sub1():
    assert 3 - 3 == 0

    @allure.title("TC#3 - verify that 1 - 1 is equals to 0")
    @allure.description("this is a smoke testcase which check - verify that 1 - 1 is equals")
    @pytest.mark.smoke
    def test_sub2():
        assert 1 - 1 == 0

        @pytest.mark.skip(reason="Not working,skip it")
        def test_sub3():
            assert 0 - 0 != 0
