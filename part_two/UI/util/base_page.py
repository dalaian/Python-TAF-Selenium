import datetime

from pip._internal.utils.deprecation import deprecated

import part_two.util.logger as logging
import time

from config import Config
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):

    __IMPLICIT_WAIT = 20
    screen_shots_path = 'UI/reports/screenshots'

    def __init__(self, driver):
        self.driver = driver
        self.browser_name = driver.capabilities['browserName']
        self.utilities = Config()

    # Common Actions

    def click(self, element):
        # TODO: looks like selenium is not able to click a Safari element using elem.click(),
        #  so, click_js() is called instead. Check if this is absolute true
        if self.browser_name == 'Safari':
            self.click_js(element)
            return
        try:
            element = self.find_element(element)
            element.click()
        except Exception as ex:
            logging.error(ex)
            raise Exception(ex)

    def safe_click(self, element, timeout=__IMPLICIT_WAIT):
        if self.browser_name == 'Safari':
            self.click_js(element, timeout)
            return
        try:
            self.wait_til_element_is_clickable(element, timeout)
            element = self.find_element(element)
            element.click()
        except Exception as ex:
            logging.error(ex)
            raise Exception(ex)

    def click_js(self, element, timeout=__IMPLICIT_WAIT):
        try:
            self.wait_til_element_is_clickable(element, timeout)
            element = self.find_element(element)
            self.driver.execute_script("arguments[0].click();", element)
        except Exception as ex:
            logging.error(ex)
            raise Exception(ex)

    def send_keys(self, element, keys, clear=True):
        try:
            element = self.find_element(element)
            if clear:
                element.clear()
            element.send_keys(keys)
        except Exception as ex:
            logging.error(ex)
            raise Exception(ex)

    def get_text(self, element, timeout=__IMPLICIT_WAIT):
        try:
            self.wait_til_element_is_clickable(element, timeout)
            element = self.find_element(element)
            # Strip the text because safari does not do that
            return element.text.strip()
        except Exception as ex:
            logging.error(ex)
            raise Exception(ex)

    def get_attribute(self, element, attribute='value'):
        try:
            element = self.find_element(element)
            return element.get_attribute(attribute)
        except Exception as ex:
            logging.error(ex)
            raise Exception(ex)

    # Checks

    def is_visible(self, element, timeout=__IMPLICIT_WAIT):
        if self.wait_for_element(element, timeout):
            return self.find_element(element).is_displayed()
        return False

    # Waits

    def wait_for_element(self, element, timeout=10):
        try:
            element = self.message_to_locator(element)
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(element))
        except Exception:
            logging.warn(self.wait_for_element, "Element " + str(element) + " was not found")
            return False
        return True

    def wait_til_element_is_clickable(self, element, timeout=__IMPLICIT_WAIT):
        try:
            element = self.message_to_locator(element)
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(element))
        except Exception:
            logging.warn(self.wait_til_element_is_clickable, "Element " + str(element) + " was not found")
            return False
        return True

    def pause(self, pause):
        time.sleep(pause)

    # Basic Actions

    def find_element(self, element):
        element = self.message_to_locator(element)
        element = self.driver.find_element(*element)
        return self.scroll_to_element(element)

    def message_to_locator(self, element):
        if isinstance(element, basestring):
            if element.startswith('//'):
                return By.XPATH, element
            else:
                return By.CSS_SELECTOR, element

        if isinstance(element, tuple):
            return element

        return None

    def scroll_to_element(self, element):
        self.driver.execute_script("return arguments[0].scrollIntoView();", element)
        return element

    # Browser
    def get(self, url):
        self.driver.get(url)

    def get_url(self):
        return self.driver.current_url

    # Extras

    def format(self, locator, value):
        return locator.format(value)

    def take_screen_shot(self, name=None, screen_shot_dir=screen_shots_path):
        if name is None or len(name) <= 0:
            name = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
        path = '{}/{}_{}.png'.format(screen_shot_dir, name, self.browser_name)
        self.driver.save_screenshot(path)
        logging.info("Screenshot was saved in : " + path)

    # Logger
    def logging(self, page, method):
        """ Deprecated: had to move the logger to another location but all the pages use this method before that
        so, a refactor is needed but don't have enough time for that.
        Note: I wanted to add the @deprecated tag but needed more time to investigate a little more
        TODO: refactor this
        :param page:
        :param method:
        :return:
        """
        logging.auto_log(page, method)
