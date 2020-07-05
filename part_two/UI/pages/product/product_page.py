from part_two.UI.locators.product.product_locators import ProductLocators
from part_two.UI.pages.cart.cart_page import CartPage
from part_two.UI.util.base_page import BasePage


class ProductPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.wait_til_element_is_clickable(ProductLocators.product_dv)

    def is_page_loaded(self):
        """ Verify if the product page is loaded
        :return: Boolean
        """
        self.logging(self, self.is_page_loaded)
        return self.is_visible(ProductLocators.product_dv)

    def get_product_title(self):
        """ Get the product title
        :return: str
        """
        self.logging(self, self.get_product_title)
        return self.get_text(ProductLocators.title_txt)

    def get_product_price(self):
        """ Get the produce price
        :return: str
        """
        self.logging(self, self.get_product_price)
        return self.get_text(ProductLocators.price_txt).replace("$", "")

    def enter_quantity(self, quantity):
        """ Enter quantity of the product
        :param quantity: int
        :return: None
        """
        self.logging(self, self.enter_quantity)
        self.send_keys(ProductLocators.quantity_inp, quantity)

    def get_quantity(self):
        """ Get the quantity
        :return: str
        """
        self.logging(self, self.get_quantity)
        return self.get_attribute(ProductLocators.quantity_inp)

    def click_add_to_cart(self):
        """ Click on add to cart button
        :return: None
        """
        self.logging(self, self.click_add_to_cart)
        self.click(ProductLocators.add_to_cart_btn)
        self.wait_for_element(ProductLocators.cart_icn)
        # Giving a little more time to load the page, since sometimes this method causes errors
        self.pause(0.8)

    def click_cart_icon(self):
        """ Click on the cart icon
        :return: None
        """
        self.logging(self, self.click_cart_icon)
        self.safe_click(ProductLocators.cart_icn)
        return CartPage(self.driver)

    def get_number_of_items_in_cart(self):
        """ Get the current number of items in the cart
        :return: str
        """
        self.logging(self, self.get_number_of_items_in_cart)
        number_of_items = self.get_text(ProductLocators.cart_items_txt)
        return number_of_items.replace(" items", "")
