import allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import LexusRegression.utilities.CustomLogger as cl
import time

class BasePage:
    log = cl.customLogger()

    def __init__(self, driver):
        self.driver = driver

    def waitForElement(self, locatorvalue, locatorType):
        locatorType = locatorType.lower()
        element = None
        wait = WebDriverWait(self.driver, 23, poll_frequency=1)

        if locatorType == "id":
            element = wait.until(lambda x: x.find_element_by_id(locatorvalue))
            return element
        elif locatorType == "accessibility id":
            element = wait.until(lambda x: x.find_element_by_accessibility_id(locatorvalue))
            return element
        elif locatorType == "class":
            element = wait.until(lambda x: x.find_element_by_class_name(locatorvalue))
            return element
        elif locatorType == "des":
            element = wait.until(
                lambda x: x.find_element_by_android_uiautomator('UiSelector().description("%s")' % (locatorvalue)))
            return element
        elif locatorType == "index":
            element = wait.until(
                lambda x: x.find_element_by_android_uiautomator("UiSelector().index(%d)" % int(locatorvalue)))
            return element
        elif locatorType == "text":
            element = wait.until(lambda x: x.find_element_by_android_uiautomator('text("%s")' % locatorvalue))
            return element
        elif locatorType == "xpath":
            element = wait.until(lambda x: x.find_element_by_xpath('%s' % locatorvalue))
            return element
        else:
            self.log.info("Locator value " + locatorvalue + "not found")

        return element

    def getElement(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            self.log.info("Element found with locatortype: "+locatorType+ " and with the locatorvalue :" +locatorValue)
        except:
            self.log.info("Element NOT found with locatortype: "+locatorType+ " and with the locatorvalue :" +locatorValue)
            self.takeScreenshot(locatorType)
            assert False
        return element

    def clickElement(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.click()
            self.log.info("clicked on element with locatortype: "+locatorType+ " and with the locatorvalue :" +locatorValue)
        except:
            self.log.info("Element NOT clickable with locatortype: "+locatorType+ " and with the locatorvalue :" +locatorValue)
            self.takeScreenshot(locatorType)
            assert False

    def sendText(self, text, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.send_keys(text)
            self.log.info("Entered text on element with locatortype: "+locatorType+ " and with the locatorvalue :" +locatorValue)
        except:
            self.log.info("Unable to send text on Element with locatortype: "+locatorType+ " and with the locatorvalue :" +locatorValue)
            self.takeScreenshot(locatorType)
            assert False


    def isDisplayed(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.is_displayed()
            self.log.info("Entered with locatortype: "+locatorType+ " and with the locatorvalue :" +locatorValue+ " is displayed")
            return True
        except:
            self.log.info("Element with locatortype: "+locatorType+ " and with the locatorvalue :" +locatorValue+ " is not displayed")
            self.takeScreenshot(locatorType)
            return False

    def screenShot(self, screenshotName):
        filename = screenshotName + "_" +(time.strftime("%d_%m_%y_%H_%M_%S")) + ".png"
        screenshotDirectory = "../screenshots/"
        screenshotPath = screenshotDirectory + filename
        try:
            self.driver.save_screenshot(screenshotPath)
            self.log.info("Screenshot saved to the path: "+screenshotPath)
        except:
            self.log.info("unable to save screenshot")

    def takeScreenshot(self, text):
        allure.attach(self.driver.get_screenshot_as_png(), name=text, attachment_type=AttachmentType.PNG)