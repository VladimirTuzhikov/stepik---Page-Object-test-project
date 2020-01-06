from pages.locators import BasketPageLocators
from pages.base_page import BasePage


class BasketPage(BasePage):
    # verify that it's a basket page
    def should_be_basket_page(self):
        self.should_be_basket_link()

    # verify that the basket is empty
    def should_be_empty_basket(self):
        basket_contents = self.browser.find_element(*BasketPageLocators.BASKET_CONTENTS)
        assert 'Your basket is empty.' in basket_contents.text, "Basket is not empty."
