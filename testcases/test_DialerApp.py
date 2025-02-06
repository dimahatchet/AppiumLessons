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
    appPackage='com.google.android.dialer',
    appActivity='com.android.dialer.main.impl.MainActivity',
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
        el = self.driver.find_element(AppiumBy.ID, value = 'com.google.android.dialer:id/dialpad_fab')
        el.click()
        time.sleep(2)
        self.driver.find_element(AppiumBy.ID, 'com.google.android.dialer:id/two').click()
        self.driver.find_element(AppiumBy.ID, 'com.google.android.dialer:id/one').click()
        self.driver.find_element(AppiumBy.ID, 'com.google.android.dialer:id/four').click()
        self.driver.find_element(AppiumBy.ID, 'com.google.android.dialer:id/dialpad_voice_call_button').click()

if __name__ == '__main__':
    unittest.main()


