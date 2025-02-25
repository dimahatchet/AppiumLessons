import time
import unittest

import allure
import pytest
from allure_commons.types import AttachmentType

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy

from pytestlearning.conftest import screen_on_failure

desired_caps = dict(

    platformName="Android",
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.google.android.calculator',
    appActivity='com.android.calculator2.Calculator',
    noReset=True

)

def get_data():
        return [
        "2",
        "4"
    ]

def setup_function():
        global appium_service
        appium_service = AppiumService()
        appium_service.start()

        appium_server_url = 'http://localhost:4723'
        capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
        global driver
        driver = webdriver.Remote(appium_server_url, options=capabilities_options)

def teardown_function():
        driver.quit()
        appium_service.stop()
@pytest.mark.usefixtures("screen_on_failure")
@pytest.mark.parametrize("number", get_data())
def test_calculator(number):
        time.sleep(2)
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, number).click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'plus').click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, number).click()
        #driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'equals').click()
        equation_result = driver.find_element(AppiumBy.ID,'com.google.android.calculator:id/result_preview').text
        print(equation_result)
        assert int(equation_result) == int(number)*2
        #allure.attach(driver.get_screenshot_as_png(),name="screen", attachment_type=AttachmentType.PNG)
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'clear').click()

if __name__ == '__main__':
    unittest.main()




