import time

from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': "uiautomator2",
    'deviceName': 'Android',
    'appPackage': 'wp.wattpad',
    'appActivity': 'wp.wattpad.ui.activities.LoginActivity',
    # 'noReset': True,
    'language': 'en',
    'locale': 'US'
}

url = 'http://localhost:4723'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
driver.implicitly_wait(30)

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

driver.find_element(by=AppiumBy.XPATH, value="//android.widget.ImageView[@content-desc='Your Profile']").click()

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(735, 1224)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@content-desc='Settings']").click()

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(414, 1875)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(435, 452)
actions.w3c_actions.pointer_action.release()
actions.perform()

driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id='android:id/title' and "
                                             "@text='Log Out']").click()


