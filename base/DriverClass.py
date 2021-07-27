from appium import webdriver
import requests
import os

class Driver:
    def getDriverMethod(self):

        # starts appium on same terminal window
        os.system("start /B start cmd.exe @cmd /k appium")

        # Browserstack integration
        files = {
            'file': ('lexus.apk', open('/Users/dineshpandiyan/PycharmProjects/pythonProject/LexusRegression/app/lexus.apk', 'rb')),
        }

        response = requests.post('https://api-cloud.browserstack.com/app-automate/upload', files=files,
                                 auth=('dineshpandiyan3', '3axvUosDbRgYYK1jhMti'))
        print(response.json()['app_url'])

        app_url = response.json()['app_url']

        userName = "dineshpandiyan3"
        accessKey = "3axvUosDbRgYYK1jhMti"

        desired_caps = {
            "build": "Python Android",
            "device": "Samsung Galaxy S8 Plus",
            "app": app_url
        }

        driver = webdriver.Remote("https://" + userName + ":" + accessKey + "@hub-cloud.browserstack.com/wd/hub",
                                  desired_caps)

        # un-comment the below code to run the script on local device

        # Step 1 : Create "Desired Capabilities"
        '''desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['automationName'] = 'UiAutomator2'
        # desired_caps['platformVersion'] = '10'
        desired_caps['deviceName'] = 'Samsung'
        # desired_caps['app'] = ('')
        desired_caps['appPackage'] = 'au.com.lexus.mylexus.app'
        desired_caps['appActivity'] = 'crc64df9d2c25963cc4a5.LaunchActivity'
        desired_caps['udid'] = 'RF8N20RCMJY'

        # Step 2 : Create "Driver object"
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)'''

        return driver