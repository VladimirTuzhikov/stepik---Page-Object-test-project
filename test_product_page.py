from pages.main_page import MainPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.locators import BasePageLocators
import pytest
import time

# parm to run pytest -v -s --tb=line --language=en-gb test_product_page.py

# test that user can add a product to the basket and the basket has the right product and price
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    link = f"{link}"
    page = MainPage(browser, link)                              # initialize Page Object, pass driver instance and url
    page.open()                                                 # open main page
    name = browser.find_element(*BasePageLocators.BOOK_NAME)    # find element with book name
    book_name = name.text                                       # save book name from the main page
    price = browser.find_element(*BasePageLocators.BOOK_PRICE)  # find element with book price
    book_price = price.text                                     # save book price from the min page
    page.go_to_product_page()                                   # go to product page by adding product to the basket
    product_page = ProductPage(browser, browser.current_url)  # initialize Page Object, pass driver instance and url
    book_name_in_basket = product_page.should_be_book_name_in_basket()    # save book name from the basket
    product_page.should_be_success_message(book_name_in_basket)           # verify that success message exists
    book_price_in_basket = product_page.should_be_book_price_in_basket()  # save book price from the basket
    print(f'Book "{book_name_in_basket}" added to basket.')  # print book name from the basket
    print(f'Basket price is {book_price_in_basket}.')        # print book price from the basket
    assert book_name == book_name_in_basket, "Book name on man page and in basket must be the same"     # verify name
    assert book_price == book_price_in_basket, "Book price on man page and in basket must be the same"  # verify price


# test that a user can't see the success message after adding product to the basket. Marked xfail.
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, product_page_url):
    page = ProductPage(browser, browser.product_page_url)       # initialize Page Object, pass driver instance and url
    page.open()                                                 # open product page
    book_name_in_basket = page.should_be_book_name_in_basket()  # save book name from the basket
    page.should_not_be_success_message(book_name_in_basket)     # verify that there is no success message


# test the a user can't see success message from the product page
def test_guest_cant_see_success_message(browser, product_page_url):
    page = ProductPage(browser, product_page_url)  # initialize Page Object, pass driver instance and url
    page.open()                                               # open product page
    name = browser.find_element(*BasePageLocators.BOOK_NAME)  # find element with book name
    book_name = name.text                                     # save book name from the main page
    page.should_not_be_success_message(book_name)             # verify that there is no success message


# test that success message disappeared after adding product to the basket. Marked xfail.
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser, product_page_url):
    page = ProductPage(browser, product_page_url)                # initialize Page Object, pass driver instance and url
    page.open()                                                      # open product page
    book_name_in_basket = page.should_be_book_name_in_basket()       # save book name from the basket
    page.should_be_disappeared_success_message(book_name_in_basket)  # verify that there is no success message


# test that a user can see the login link on the product page
def test_guest_should_see_login_link_on_product_page(browser, product_page_url):
    page = ProductPage(browser, product_page_url)  # initialize Page Object, pass driver instance and url address
    page.open()                                    # open product page
    page.should_be_login_link()                    # verify that 'Login or register' form is presents


# test that a user can't see a product in the basket opened from the main page
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser, main_page_url):
    page = ProductPage(browser, main_page_url)  # initialize Page Object, pass driver instance and url
    page.open()                                    # open main page
    page.should_be_basket_link()                   # verify that 'View basket' button is present
    page.go_to_basket_page()                       # go to basket page by clicking 'View basket' button
    basket_page = BasketPage(browser, browser.current_url)  # initialize Page Object, pass driver instance and url
    basket_page.should_be_empty_basket()                    # verify that basket is empty


# test that a user can go to the login page from the product page
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser, product_page_url):
    page = ProductPage(browser, product_page_url)  # initialize Page Object, pass driver instance and url address
    page.open()                                    # open product page
    page.go_to_login_page()                        # execute page method - go to login page
    login_page = LoginPage(browser, browser.current_url)  # initialize Page Object, pass driver instance and url
    login_page.should_be_login_page()                     # verify that it's login page


@pytest.mark.login_user
class TestUserAddToBasketFromProductPage():

    # set up to be run automatically for all tests within this class: open product page and register a new user
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, product_page_url):
        page = MainPage(browser, product_page_url)                # initialize Page Object, pass driver instance and url
        page.open()                                                # open product page
        link = browser.find_element(*BasePageLocators.LOGIN_LINK)  # find login link
        link.click()                                               # click it
        email = str(time.time()) + "@fakemail.org"                 # generate an email, to have unique use time
        password = 'RegistrationPassword'                          # set password
        login_page = LoginPage(browser, browser.current_url)  # initialize Page Object, pass driver instance and url
        login_page.should_be_login_page()                     # verify that it's login page
        login_page.register_new_user(email, password)         # register a new user using email and password

    # test that user can't see success message on the product page
    def test_user_cant_see_success_message(self, browser, product_page_url):
        page = ProductPage(browser, product_page_url)             # initialize Page Object, pass driver instance and url
        page.open()                                               # open product page
        name = browser.find_element(*BasePageLocators.BOOK_NAME)  # find element with book name
        book_name = name.text                                     # save book name from the main page
        page.should_not_be_success_message(book_name)             # verify that there is no success message

    # test that user can add a product to the basket and the basket has the right product and price
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, product_page_url):
        page = MainPage(browser, product_page_url)                # initialize Page Object, pass driver instance and url
        page.open()                                               # open product page
        name = browser.find_element(*BasePageLocators.BOOK_NAME)  # find element with book name
        book_name = name.text  # save book name from the main page
        price = browser.find_element(*BasePageLocators.BOOK_PRICE)  # find element with book price
        book_price = price.text  # save book price from the min page
        page.go_to_product_page()  # go to product page by adding product to the basket
        product_page = ProductPage(browser, browser.current_url)  # initialize Page Object, pass driver instance and url
        book_name_in_basket = product_page.should_be_book_name_in_basket()  # save book name from the basket
        product_page.should_be_success_message(book_name_in_basket)  # verify that success message exists
        book_price_in_basket = product_page.should_be_book_price_in_basket()  # save book price from the basket
        print(f'Book "{book_name_in_basket}" added to basket.')  # print book name from the basket
        print(f'Basket price is {book_price_in_basket}.')  # print book price from the basket
        assert book_name == book_name_in_basket, "Book name on man page and in basket must be the same"  # verify name
        assert book_price == book_price_in_basket, "Book price on man page and in basket must be the same"  # verify price
