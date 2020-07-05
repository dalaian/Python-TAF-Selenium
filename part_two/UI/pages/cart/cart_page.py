from part_two.UI.locators.cart.cart_locators import CartLocators
from part_two.UI.util.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.wait_til_element_is_clickable(CartLocators.proceed_checkout_btn)

    def is_product_visible(self, product_name):
        """ Check if the product is visible
        :param product_name: str
        :return: Boolean
        """
        self.logging(self, self.is_product_visible)
        locator = self.format(CartLocators.product_name_txt, product_name)
        return self.is_visible(locator)

    def get_product_price(self, product_name):
        """ Get the price of a given product
        :param product_name: str
        :return: str
        """
        self.logging(self, self.get_product_price)
        locator = self.format(CartLocators.product_price_txt, product_name)
        return self.get_text(locator).replace("$", '')

    def get_product_quantity(self, product_name):
        """ Get the quantity of a given product
        :param product_name: str
        :return: str
        """
        self.logging(self, self.get_product_quantity)
        locator = self.format(CartLocators.product_quantity_txt, product_name)
        return self.get_attribute(locator)

    def get_product_total(self, product_name):
        """ Get the total of a given product
        :param product_name: str
        :return: str
        """
        self.logging(self, self.get_product_total)
        locator = self.format(CartLocators.product_total_txt, product_name)
        return self.get_text(locator).replace("$", '')
