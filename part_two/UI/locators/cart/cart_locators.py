from selenium.webdriver.common.by import By


class CartLocators(object):

    product_name_txt = "//td[@class='product-name']/a[text()='{}']"
    product_row = product_name_txt + "/ancestor::tr"
    product_price_txt = product_row + "/td[@class='product-price']"
    product_quantity_txt = product_row + "/td[@class='product-quantity']//input"
    product_total_txt = product_row + "/td[@class='product-subtotal']"

    proceed_checkout_btn = (By.CSS_SELECTOR, "a.checkout-button")
