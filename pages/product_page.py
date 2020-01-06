from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.can_add_product_to_basket()
        self.should_be_book_name_in_basket()
        self.should_be_book_price_in_basket()
        self.should_be_success_message()
        self.should_not_be_success_message()
        self.should_be_disappeared_success_message()

    def can_add_product_to_basket(self):
        self.solve_quiz_and_get_code()

    def should_be_book_name_in_basket(self):
        name = self.browser.find_element(*ProductPageLocators.ADDED_BOOK_NAME)
        return name.text

    def should_be_book_price_in_basket(self):
        price = self.browser.find_element(*ProductPageLocators.ADDED_BOOK_PRICE)
        return price.text

    def should_be_success_message(self, success_message_text):
        assert self.is_element_present(*ProductPageLocators(success_message_text).SUCCESS_MESSAGE), \
            "Success message is not present, but should"

    def should_not_be_success_message(self, success_message_text):
        assert self.is_not_element_present(*ProductPageLocators(success_message_text).SUCCESS_MESSAGE), \
            "Success message is present, but should not be"

    def should_be_disappeared_success_message(self, success_message_text):
        assert self.is_disappeared(*ProductPageLocators(success_message_text).SUCCESS_MESSAGE), \
            "Success message is present, but should be disappeared"

