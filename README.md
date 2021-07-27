# APPIUM - PYTHON - POM

# Pre-requisite
  1.APPIUM installed
  2.ANDROID_HOME & JAVA_HOME are set correctly
  
# Setup
  Clone the project
  Run the following shell command to download all the dependencies
  $ python3 -m pip install -r requirements.txt
  
# Change the app under the app folder present in the root directory and update the file path present under 'DriverClass.py'
  
  # Browserstack integration
        files = {
            'file': ('lexus.apk', open('/Users/dineshpandiyan/PycharmProjects/pythonProject/LexusRegression/app/lexus.apk', 'rb')),
        }

# Framework has been configured to run both local devices and cloud service like (Browserstack)

# Update the desired device settings under 'DriverClass.py'
  
   desired_caps = {
            "build": "Python Android",
            "device": "Samsung Galaxy S8 Plus",
            "app": app_url
        }
 
# To run the test - execute the following command
  py.test --alluredir=/Users/dineshpandiyan/PycharmProjects/pythonProject/LexusRegression/reports/allurereports LoginTest.py
 
# Run the below command to generate html report
  allure serve ../reports/allurereports   

