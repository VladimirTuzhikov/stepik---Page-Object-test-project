from pages.main_page import MainPage
from pages.login_page import LoginPage


# test that after going to the login page from the main the url is the login url
def test_should_be_login_url(browser, link):
    page = MainPage(browser, link)   # initialize Page Object, pass driver instance and url address
    page.open()                      # open main page
    page.go_to_login_page()          # go to login page by clicking 'Login or register' form
    login_page = LoginPage(browser, browser.current_url)  # initialize Page Object, pass driver instance and url
    login_page.should_be_login_url()                      # verify that current url is a login url


# test that after going to the login page from the main there is the login form
def test_guest_should_see_login_form(browser, link):
    page = MainPage(browser, link)   # initialize Page Object, pass driver instance and url address
    page.open()                      # open main page
    page.go_to_login_page()          # go to login page by clicking 'Login or register' form
    login_page = LoginPage(browser, browser.current_url)  # initialize Page Object, pass driver instance and url
    login_page.should_be_login_form()                     # verify that login form is present


# test that after going to the login page from the main there is the register form
def test_guest_should_see_register_form(browser, link):
    page = MainPage(browser, link)   # initialize Page Object, pass driver instance and url address
    page.open()                      # open main page
    page.go_to_login_page()          # go to login page by clicking 'Login or register' form
    login_page = LoginPage(browser, browser.current_url)  # initialize Page Object, pass driver instance and url address
    login_page.should_be_register_form()                  # verify that register form is present

