from selenium.webdriver.common.by import By


class BasePageLocators:  # base page locators
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")                           # login link
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")               # invalid  login link
    ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form button")         # 'Add to basket' button
    BOOK_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main>h1")              # book name
    BOOK_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main p.price_color")  # book price
    BASKET_LINK = (By.CSS_SELECTOR, 'span.btn-group a')                     # basket link
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")                             # user icon


class LoginPageLocators:  # login page locators
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")                       # login form
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")                 # register form
    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")             # fill registration email
    REG_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")      # fill registration password
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")  # confirm registration password


class ProductPageLocators:  # product page locators

    def __init__(self, success_message_text):
        self.SUCCESS_MESSAGE = (By.XPATH, '//*[contains(@class, "alert alert-safe")][1]'
                                          '[contains(.,"' + success_message_text + '")]')  # success message

    ADDED_BOOK_NAME = (By.XPATH, '//*[contains(@class, "alertinner ")][1]/strong')         # added book name
    ADDED_BOOK_PRICE = (By.CSS_SELECTOR, ".alertinner >p>strong")                          # added book price


class BasketPageLocators:
    BASKET_CONTENTS = (By.CSS_SELECTOR, ".content #content_inner>p")  # Element existing only when basket is empty

