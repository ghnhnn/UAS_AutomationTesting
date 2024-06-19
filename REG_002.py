import time

from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': "uiautomator2",
    'deviceName': 'Android',
    'appPackage': 'wp.wattpad',
    'appActivity': 'wp.wattpad.ui.activities.LoginActivity',
    'language': 'en',
    'locale': 'US'
}

url = 'http://localhost:4723'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
driver.implicitly_wait(25)

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Join for free").click()

driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text='Email']").send_keys("jstclds@gmail.com")
time.sleep(5)

driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text='Username']").send_keys("CldsUASPKPL")
time.sleep(5)

driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text='Password']").send_keys("WpUAS123")
time.sleep(5)

driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView["
                                             "@resource-id='wp.wattpad:id/field_content_show']").click()
time.sleep(10)

driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView["
                                             "@resource-id='wp.wattpad:id/field_content_show']").click()
# driver.implicitly_wait(10)

# driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView["
#                                              "@resource-id='wp.wattpad:id/authentication_view_dob_field']").click()
# driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text='May']").click()
# driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text='12']").click()
# driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text='2000']").click()
# driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="SET").click()
