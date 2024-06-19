import time

from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': "uiautomator2",
    'deviceName': 'Android'
}

url = 'http://localhost:4723'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="Chrome"]')
el.click()

driver.find_element(by=AppiumBy.XPATH, value="//*[@text='Search or type web address']").send_keys("Tes UTS Ghinaa")
