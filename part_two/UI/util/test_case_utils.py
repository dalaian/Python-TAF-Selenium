import argparse
import collections
import sys
import traceback
from distutils.util import strtobool

from part_two.API.product.product import Product
from part_two.UI.util.config import Config
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
import part_two.util.logger as logger


class TestCaseUtils:
    __IMPLICIT_WAIT = 10
    cmd_line_args = None

    def __init__(self, test_case=None):
        self.parser = None
        self.config = Config()
        self.driver = None
        if test_case is not None:
            self.browser = test_case.BROWSER
            self.headless = test_case.HEAD_LESS
            logger.config_logger(test_case.__name__, self.browser)

    def open_browser(self):
        grid = self.config.get_grid()
        if self.browser == 'CHROME':
            capabilities = DesiredCapabilities.CHROME
            if self.headless:
                capabilities["chromeOptions"] = {"args": ['headless', 'no-sandbox', 'disable-gpu',
                                                          'window-size=1920x1080']}
        elif self.browser == 'FIREFOX':
            capabilities = DesiredCapabilities.FIREFOX
            if self.headless:
                capabilities["moz:firefoxOptions"] = {"args": ['-headless']}
        elif self.browser == 'SAFARI':
            capabilities = DesiredCapabilities.SAFARI
            if self.headless:
                raise Exception("Not able to support Safari Headless")
        else:
            capabilities = DesiredCapabilities.CHROME

        self.driver = webdriver.Remote(grid, desired_capabilities=capabilities)
        self.driver.implicitly_wait(TestCaseUtils.__IMPLICIT_WAIT)
        self.driver.maximize_window()
        return self.driver

    def url(self, url=None):
        if url is None:
            url = self.config.get_base_url()
        self.driver.get(url)

    def tear_down(self, test):
        exc_info = sys.exc_info()
        if exc_info[0]:
            logger.error(exc_info[1])
            logger.error(traceback.format_exc())
            if test.page is not None:
                test.page.take_screen_shot(str(test.__class__.__name__ + '_' + test._testMethodName))

    def close(self):
        self.driver.quit()

    # API

    def create_product_api(self):
        url = self.config.get_base_url()
        user_api = self.config.get_api_user()
        return Product(url, user_api)

    # CLI

    def get_variables_from_command_line(self):
        self.parser.add_argument(
            '-b',
            '--browser',
            dest='browser',
            nargs='?',
            required=False,
            const='CHROME',
            default='CHROME',
            help='The browser in which the TC will be executed, by default CHROME'
        )
        self.parser.add_argument(
            '-hl',
            '--headless',
            dest='headless',
            nargs='?',
            required=False,
            const='False',
            default='False',
            help='Indicates whether the test should be executed in headless mode, by default False'
        )
        args = collections.deque(sys.argv)
        args.popleft()
        return self.parser.parse_args(args)

    def set_parameters_to_this(self, test_case):
        self.parser = argparse.ArgumentParser()
        if TestCaseUtils.cmd_line_args is None:
            TestCaseUtils.cmd_line_args = self.get_variables_from_command_line()
        cmd_line_args = TestCaseUtils.cmd_line_args

        test_case.BROWSER = cmd_line_args.browser
        test_case.HEAD_LESS = strtobool(cmd_line_args.headless)

        del sys.argv[1:]
        return test_case
