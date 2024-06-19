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

el10 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Create new contact")
el10.click()
driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@text='CANCEL']").click()
el11 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"First name\")")
el11.click()
el11.send_keys("Ghinaa1")
el12 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Phone\")")
el12.click()
el12.send_keys("082320108171")
el13 = driver.find_element(by=AppiumBy.ID, value="com.android.contacts:id/editor_menu_save_button")
el13.click()

