from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': "uiautomator2",
    'deviceName': 'Android',
    'appPackage': 'com.android.contacts',
    'appActivity': '.activities.PeopleActivity',
    'language': 'en',
    'locale': 'US'
}

url = 'http://localhost:4723'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
driver.implicitly_wait(10)

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Create new contact").click()

driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@text='CANCEL']").click()

driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text='First name']").send_keys("Ghinaa")

driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text='Phone']").send_keys("082120108171")

driver.find_element(by=AppiumBy.XPATH, value=" //android.widget.Button[@text='SAVE']").click()