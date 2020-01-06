from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    # verify that url address is for login page
    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "'login' is not in URL."

    # verify that login form presents
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    # verify that registration form presents
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present"

    # register a new user
    def register_new_user(self, email, password):
        input1 = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        input1.send_keys(email)
        input2 = self.browser.find_element(*LoginPageLocators.REG_PASSWORD)
        input2.send_keys(password)
        input2 = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        input2.send_keys(password)
