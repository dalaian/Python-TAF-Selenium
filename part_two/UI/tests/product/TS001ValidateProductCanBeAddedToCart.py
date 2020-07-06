import importer
import part_two.util.read_file as read_file
import unittest
import xmlrunner

from part_two.UI.pages.product.product_page import ProductPage
from part_two.UI.util.test_case_utils import TestCaseUtils


class TS001ValidateProductCanBeAddedToCart(unittest.TestCase):

    BROWSER = 'CHROME'  # Options: CHROME, FIREFOX, SAFARI
    HEAD_LESS = False

    @classmethod
    def setUpClass(cls):
        cls.utils = TestCaseUtils(cls)
        cls.data = read_file.read_data_file("product/TS001ValidateProductCanBeAddedToCart.json")
        cls.productAPI = cls.utils.create_product_api()

    def test_00_preconditions(self):
        self.data["product_api"] = self.productAPI.create(self.data["product"])

    def test_01_navigation(self):
        driver = self.utils.open_browser()
        self.utils.url(self.data["product_api"]["permalink"])
        self.__class__.page = ProductPage(driver)

        self.assertTrue(self.page.is_page_loaded(), "Product page did not load")
        self.assertEqual(self.page.get_product_title(), self.data["product"]["name"],
                         "The price of the product is not correct")
        self.assertEqual(self.page.get_product_price(), self.data["product"]["regular_price"],
                         "The price of the product is not correct")

    def test_02_increase_quantity(self):
        self.page.enter_quantity(self.data["quantity"])
        self.assertEqual(self.page.get_quantity(), self.data["quantity"],
                         "The quantity is not right")

    def test_03_add_to_cart(self):
        self.page.click_add_to_cart()
        self.assertEqual(self.page.get_number_of_items_in_cart(), self.data["quantity"],
                         "The amount of items in the cart is not correct")

    def test_04_click_cart_icon(self):
        self.page = self.page.click_cart_icon()
        product_name = self.data["product"]["name"]

        self.assertEqual(self.page.get_url(), self.utils.config.get_base_url() + self.data["url"],
                         "The URL is not the expected one")
        self.assertTrue(self.page.is_product_visible(product_name), "Product is not in the cart")
        self.assertEqual(self.page.get_product_price(product_name), self.data["product"]["regular_price"],
                         "The price of the product {} is not correct".format(product_name))
        self.assertEqual(self.page.get_product_quantity(product_name), self.data["quantity"],
                         "The quantity of the product {} is not correct".format(product_name))
        self.assertEqual(self.page.get_product_total(product_name), self.data["total"],
                         "The total price of the product {} is not correct".format(product_name))

    def tearDown(self):
        self.utils.tear_down(self)

    @classmethod
    def tearDownClass(cls):
        cls.utils.close()
        cls.productAPI.delete(cls.data["product_api"]["id"])


if __name__ == '__main__':
    TestCaseUtils().set_parameters_to_this(TS001ValidateProductCanBeAddedToCart)
    with open('UI/reports/TS001ValidateProductCanBeAddedToCart.xml', 'wb') as output:
        unittest.main(testRunner=xmlrunner.XMLTestRunner(output=output, verbosity=2),
                      failfast=False, buffer=False, catchbreak=False)
