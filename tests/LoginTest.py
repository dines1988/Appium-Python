import unittest
import pytest
import LexusRegression.utilities.CustomLogger as cl
from LexusRegression.pages.LoginPage import Login

@pytest.mark.usefixtures("beforeClass","beforeMethod")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.lp = Login(self.driver)

    @pytest.mark.run(order=1)
    #log.info("Test log")
    def test_login(self):
        cl.allurelogs("App Launched")
        self.lp.launchPage()
        self.lp.verifyloginPage()
        self.lp.login()



