from LexusRegression.base.BasePage import BasePage
import LexusRegression.utilities.CustomLogger as cl

class Dashboard(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators in login page
    _pageTitle = "JIMMY"  # text
