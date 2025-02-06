import time

import allure
import openpyxl
import pytest
import unittest
from allure_commons.types import AttachmentType
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy

from testcases.scroll_util import ScrollUtil
from utilities import dataProvider

desired_caps = dict(

    platformName="Android",
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.google.android.calculator',
    appActivity='com.android.calculator2.Calculator',
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

@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.parametrize("city,country", dataProvider.get_data("SearchTest"))
def test_dologin(city,country,appium_driver):
     driver = appium_driver
     driver.find_element_by_id('com.goibibo:id/btn1').click()
     driver.find_element_by_accessibility_id('destination').click()
     driver.find_element_by_id('com.goibibo:id/edtSearch').send_keys(city)
     driver.find_elements_by_id('com.goibibo:id/lytLocationItem')[0].click()
     driver.find_element_by_xpath("//android.widget.TextView[@text='Search']").click()
     cityText = driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'EXPLORE')]").text
     print(cityText)
     newCityText = str(cityText).replace("EXPLORE ","").replace("!","")
     print(newCityText)

     assert newCityText in str(city).upper()
     #allure.attach(driver.get_screenshot_as_png(),name="screenshot",attachment_type=AttachmentType.PNG)




def test_searchVillas(appium_driver):
    driver = appium_driver
    driver.find_element_by_xpath("//android.widget.TextView[@text='Villas & Apts']").click()
    driver.find_element_by_xpath("//android.widget.TextView[@text='Area, Landmark or Property']").click()
    driver.find_element_by_id('com.goibibo:id/edtSearch').send_keys("Delhi")
    driver.hide_keyboard()
    #driver.find_elements_by_id('com.goibibo:id/lytLocationItem')[0].click()
    #driver.find_element_by_xpath("//android.widget.TextView[@text='6']").click()
    #driver.find_element_by_xpath("//android.widget.TextView[@text='11']").click()
    #driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'Continue')]").click()
    #driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'View Stays')]").click()
    #ScrollUtil.scrollToTextByAndroidUIAutomator("Shubham Vilas", driver)

if __name__ == '__main__':
    unittest.main()

