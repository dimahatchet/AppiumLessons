import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
#from appium.webdriver.common.touch_action import TouchAction

from testcases.scroll_util import ScrollUtil

desired_caps = dict(

    platformName="Android",
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='flipboard.app',
    appActivity='flipboard.activities.LaunchActivityAlias',
    language='en',
    locale='US'

)
appium_service = AppiumService()
appium_service.start()

appium_server_url = 'http://localhost:4723'
capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote(appium_server_url, options=capabilities_options)
driver.implicitly_wait(10)


driver.find_element(AppiumBy.ID,'flipboard.app:id/first_launch_get_started_button').click()

driver.find_elements(AppiumBy.ID,'flipboard.app:id/topic_picker_topic_row_topic_tag')[0].click()
driver.find_elements(AppiumBy.ID,'flipboard.app:id/topic_picker_topic_row_topic_tag')[1].click()
driver.find_elements(AppiumBy.ID,'flipboard.app:id/topic_picker_topic_row_topic_tag')[2].click()
driver.find_element(AppiumBy.ID,'flipboard.app:id/topic_picker_continue_button').click()
driver.find_element(AppiumBy.ID,'flipboard.app:id/account_login_buttons_skip').click()
time.sleep(2)

ScrollUtil.swipeUpNew(4,driver)
time.sleep(2)
ScrollUtil.swipeDownNew(4,driver)
time.sleep(2)
ScrollUtil.swipeLeftNew(2,driver)
time.sleep(2)
ScrollUtil.swipeRightNew(2,driver)

time.sleep(2)
driver.quit()
