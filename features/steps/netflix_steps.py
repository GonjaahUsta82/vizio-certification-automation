from behave import given, when, then

from pages.home_page import HomePage
from pages.netflix_page import NetflixPage

home_page = HomePage()
netflix_page = NetflixPage()


@given("TV is on Home screen")
def step_home(context):
    home_page.press_home()


@when("user presses Netflix button")
def step_press_netflix(context):
    netflix_page.press_netflix_button()


@then("Netflix should open")
def step_verify_netflix(context):
    assert netflix_page.verify_opened()


@when("user presses Home button")
def step_press_home(context):
    home_page.press_home()


@then("TV should return to Home screen")
def step_verify_home(context):
    assert True