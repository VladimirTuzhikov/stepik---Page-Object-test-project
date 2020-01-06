from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

# parm to run pytest -v -s --tb=line --language=en-gb test_main_page.py


# test that a user can go to the login page from the main page
def test_guest_can_go_to_login_page(browser, main_page_url):
    page = MainPage(browser, main_page_url)  # initialize Page Object, pass driver instance and url
    page.open()                              # open main page
    page.go_to_login_page()                  # go to login page by clicking 'Login or register' form
    login_page = LoginPage(browser, browser.current_url)  # initialize Page Object, pass driver instance and url
    login_page.should_be_login_page()                     # verify that it's login page


# test that a user cn see the login link on the main page
def test_guest_should_see_login_link(browser, main_page_url):
    page = MainPage(browser, main_page_url)  # initialize Page Object, pass driver instance and url
    page.open()                              # open main page
    page.should_be_login_link()              # verify that 'Login or register' is present


# test that a user can't see a product in the basket opened from the main page
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser, main_page_url):
    page = MainPage(browser, main_page_url)  # initialize Page Object, pass driver instance and url
    page.open()                              # open main page
    page.should_be_basket_link()             # verify that 'View basket' button is present
    page.go_to_basket_page()                 # go to basket page by clicking 'View basket' button
    basket_page = BasketPage(browser, browser.current_url)  # initialize Page Object, pass driver instance and url
    basket_page.should_be_empty_basket()                    # verify that basket is empty

