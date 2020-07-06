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
        """ Open the browser depending on the value of BROWSER
        @return: webdriver
        """
        # gets the url of the grid
        grid = self.config.get_grid()

        # decide what browser to open based on BROWSER and if should run headless
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

        # opens the browser using the grid
        self.driver = webdriver.Remote(grid, desired_capabilities=capabilities)
        # sets the implicit wait value
        self.driver.implicitly_wait(TestCaseUtils.__IMPLICIT_WAIT)
        # maximize de window to avoid any issue related to the size of the screen
        self.driver.maximize_window()
        return self.driver

    def url(self, url=None):
        """ Go to a given url
        @param url: str, url to go, by default it will go to the base url
        @return: None
        """
        if url is None:
            # get the base url
            url = self.config.get_base_url()
        self.driver.get(url)

    def tear_down(self, test):
        """ Actions to do every time a test method is finished
        @param test: test
        @return: None
        """
        # gets the execution info
        exc_info = sys.exc_info()

        # checks if there's an error in the execution of the test
        if exc_info[0]:
            # if there's an error, log the error
            logger.error(exc_info[1])
            logger.error(traceback.format_exc())
            # if there's a page in the test, takes the screen of it
            if test.page is not None:
                test.page.take_screen_shot(str(test.__class__.__name__ + '_' + test._testMethodName))

    def close(self):
        """ Actions to do after a test case ends
        @return: None
        """
        # close the browser
        self.driver.quit()

    # API

    def create_product_api(self):
        """ Create a Product class to interact with the API
        @return: Product
        """
        # gets the base url to the API
        url = self.config.get_base_url()
        # gets the credentials to use the API
        user_api = self.config.get_api_user()
        return Product(url, user_api)

    # CLI

    def get_variables_from_command_line(self):
        """ Get the variables from the command line and gives all the information needed to add the -h parameter
        @return: the arguments
        """
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

    def set_parameters_to_test_case(self, test_case):
        """ Sets the parameters from the console, to the test case
        @param test_case: test case with the parameter all set to run
        @return: test_case
        """
        self.parser = argparse.ArgumentParser()
        if TestCaseUtils.cmd_line_args is None:
            TestCaseUtils.cmd_line_args = self.get_variables_from_command_line()
        cmd_line_args = TestCaseUtils.cmd_line_args

        # set the values of the command line to the test case
        test_case.BROWSER = cmd_line_args.browser
        test_case.HEAD_LESS = strtobool(cmd_line_args.headless)

        # deletes the arguments because unittest won't run if it has arguments
        del sys.argv[1:]
        return test_case
