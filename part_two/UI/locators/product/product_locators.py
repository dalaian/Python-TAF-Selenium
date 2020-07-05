from selenium.webdriver.common.by import By


class ProductLocators(object):

    product_dv = (By.CSS_SELECTOR, "div.product")

    title_txt = (By.CSS_SELECTOR, "h1.product_title")
    price_txt = (By.CSS_SELECTOR, ".entry-summary .price")
    quantity_inp = (By.CSS_SELECTOR, "input[name='quantity']")
    add_to_cart_btn = (By.CSS_SELECTOR, "button[name='add-to-cart']")

    view_cart_lnk = (By.CSS_SELECTOR, ".woocommerce-message a[href$='/cart/']")

    cart_icn = (By.CSS_SELECTOR, "a.cart-contents")
    cart_items_txt = (By.CSS_SELECTOR, ".cart-contents .count")
    cart_amount_txt = (By.CSS_SELECTOR, ".cart-contents .amount")
