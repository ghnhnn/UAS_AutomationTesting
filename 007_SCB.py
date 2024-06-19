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
    # "noReset": True,
    'language': 'en',
    'locale': 'US'
}

url = 'http://localhost:4723'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
driver.implicitly_wait(10)

driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id='wp.wattpad:id/log_in_button']").click()

driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText["
                                             "@resource-id='wp.wattpad:id/validate_content_field' and "
                                             "@text='Username']").send_keys(
                                             "CldsUASPKPL")
driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText["
                                             "@resource-id='wp.wattpad:id/validate_content_field' and "
                                             "@text='Password']").send_keys(
                                             "WpUAS1234#")
driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView["
                                             "@resource-id='wp.wattpad:id/authentication_view_native_auth_button']").click()

driver.find_element(by=AppiumBy.XPATH, value="//android.widget.ImageButton[@content-desc='Search']").click()

driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText["
                                             "@resource-id='wp.wattpad:id/discover_search_search_bar_prompt']").send_keys("Sahabat")
driver.press_keycode(66)

# driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id='wp.wattpad:id/list_item_title' "
#                                              "and @text='sahabat sejati']").click()
#
# driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@resource-id='wp.wattpad:id/touch_outside']").click()