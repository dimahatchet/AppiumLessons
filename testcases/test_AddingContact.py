import time
import unittest

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy

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


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=capabilities_options)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()
        appium_service.stop()

    def test_dialer(self) -> None:
        el = self.driver.find_element(AppiumBy.ID, value = 'com.google.android.contacts:id/contacts')
        time.sleep(2)
        el.click()

        self.driver.find_element(AppiumBy.ID, 'com.google.android.contacts:id/floating_action_button').click()
        self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="First name"]').send_keys("Dima")
        self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="Last name"]').send_keys("Python")
        self.driver.hide_keyboard()
        self.driver.find_element(AppiumBy.XPATH,"//*[contains(@text,'Save')]").click()
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(8)').click()
if __name__ == '__main__':
    unittest.main()

    driver = webdriver.Remote(appium_server_url, options=capabilities_options)
    el1 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, value="Create contact")
    el1.click()
    el2 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"First name\")")
    el2.click()
    el2.send_keys("Dima")
    el3 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Last name\")")
    el3.click()
    el3.send_keys("Python")
    el4 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,value="new UiSelector().className(\"android.widget.Button\").instance(4)")
    el4.click()