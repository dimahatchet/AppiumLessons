import time
import unittest
from argparse import Action

from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

#from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import TouchActions, ActionChains
#from selenium.webdriver.common.by import By

from testcases.scroll_util import ScrollUtil

desired_caps = dict(

    platformName="Android",
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.google.android.contacts',
    appActivity='com.google.android.apps.contacts.activities.PeopleActivity',
    language='en',
    locale='US'

)

appium_service = AppiumService()
appium_service.start()

appium_server_url = 'http://localhost:4723'
capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote(appium_server_url, options=capabilities_options)
driver.implicitly_wait(10)

#value ="hello";
#driver.find_element_by_android_uiautomator('new UiSelector().text(',value,')').click()


ScrollUtil.scrollToTextByAndroidUIAutomator("Akash",driver)
#driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("Akash").instance(0))').click()
#driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("Akash").instance(0))')).click()

#el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("Akash").instance(0))')
#action = TouchAction(driver)
#action.long_press(el).perform()


# driver.swipe(514,600,514,200,1000)
# driver.swipe(514,600,514,200,1000)
# driver.swipe(514,600,514,200,1000)
# driver.swipe(514,600,514,200,1000)
#
#
# driver.swipe(514,500,514,800,1000)
# driver.swipe(514,500,514,800,1000)
# driver.swipe(514,500,514,800,1000)
# driver.swipe(514,500,514,800,1000)

ScrollUtil.swipeUp(4,driver)
ScrollUtil.swipeDown(4,driver)
elements = driver.find_elements(AppiumBy.ID,'com.android.contacts:id/cliv_name_textview')
# print(len(elements))
#
actions = ActionChains(driver)
actions.click(elements[2])
# actions.long_press(elements[2])
# actions.perform()
#
#

time.sleep(2)
driver.quit()
