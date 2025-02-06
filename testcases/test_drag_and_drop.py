import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains

desired_caps = dict(

    platformName="Android",
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.mobeta.android.demodslv',
    appActivity='.Launcher',
    language='en',
    locale='US'

)
appium_service = AppiumService()
appium_service.start()

appium_server_url = 'http://localhost:4723'
capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote(appium_server_url, options=capabilities_options)
driver.implicitly_wait(10)

if driver.find_element(AppiumBy.ID,"com.android.permissioncontroller:id/continue_button").is_displayed():
    driver.find_element(AppiumBy.ID,"com.android.permissioncontroller:id/continue_button").click()

#driver.find_element(AppiumBy.LINK_TEXT, "OK").click()
driver.implicitly_wait(10)
driver.find_elements(AppiumBy.ID,'com.mobeta.android.demodslv:id/activity_title')[0].click()
#driver.find_elements_by_id('com.mobeta.android.demodslv:id/activity_title')[0].click()

elements = driver.find_elements(AppiumBy.ID,'com.mobeta.android.demodslv:id/drag_handle')

actions = ActionChains(driver)
actions.click_and_hold(elements[0])
actions.move_to_element(elements[3])
actions.release(elements[3])
actions.perform()

time.sleep(2)
driver.quit()