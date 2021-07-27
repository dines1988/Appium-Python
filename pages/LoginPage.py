from LexusRegression.base.BasePage import BasePage
import LexusRegression.utilities.CustomLogger as cl

class Login(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators in login page
    _pageTitle = "DISCOVER" #text
    _pageTitle2 = "THE WORLD" #text
    _pageTitle3 = "OF LEXUS"  #text
    _signinButton = "BtnSignIn_Container" #accessibility
    _registerButton = "BtnRegister_Container" #accessibility

    _loginTitle = "3" # index
    _username = "android.widget.EditText" #class
    _password = "(//android.widget.EditText)[2]" #xpath
    _forgotPwd = "Forgot password?" #text
    _notRegistered = "Not registered yet?"  #text
    _loginButton ="android.widget.Button" #class

    def launchPage(self):
        cl.allurelogs("Launched Lexus Encore App")
        element1 = self.isDisplayed(self._pageTitle, "text")
        element2 = self.isDisplayed(self._pageTitle2, "text")
        element3 = self.isDisplayed(self._pageTitle3, "text")
        assert element1 == True
        assert element2 == True
        assert element3 == True

    def verifyloginPage(self):
        cl.allurelogs("Login page opened")
        self.clickElement(self._signinButton, "accessibility id")
        element = self.isDisplayed(self._loginTitle, "index")
        element2 = self.isDisplayed(self._username, "class")
        element3 = self.isDisplayed(self._password, "xpath")
        element4 = self.isDisplayed(self._forgotPwd, "text")
        element5 = self.isDisplayed(self._notRegistered, "text")
        element6 = self.isDisplayed(self._loginButton, "class")
        assert element == True
        assert element2 == True
        assert element3 == True
        assert element4 == True
        assert element5 == True
        assert element6 == True

    def login(self):
        cl.allurelogs("Clicked login...")
        self.sendText("jimmy.james@mailinator.com", self._username, "class")
        self.sendText("Test12345!", self._password, "xpath")
        self.clickElement(self._loginButton, "class")






