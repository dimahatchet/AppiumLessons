import time
import unittest
import pytest

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = dict(

    platformName="Android",
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.google.android.calculator',
    appActivity='com.android.calculator2.Calculator',
    noReset=True

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

    def test_calculator(self) -> None:
        time.sleep(2)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '2').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'plus').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '4').click()
        #self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'equals').click()
        equation_result = self.driver.find_element(AppiumBy.ID,'com.google.android.calculator:id/result_preview').text
        print(equation_result)
        assert int(equation_result) == 6

if __name__ == '__main__':
    unittest.main()




