from pathlib import Path
import time
import unittest
import pytest

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v85.fetch import continue_request
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desired_caps = {'platformName': 'Android',
                'deviceName': 'Android',
                'app': str(Path().absolute().parent) + '\\app\\app-release.apk',
                'appPackage': 'com.forshared.reader',
                'appActivity': '.MainActivity'
                }

appium_service = AppiumService()
appium_service.start()

appium_server_url = 'http://localhost:4723'
capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)

driver = webdriver.Remote(appium_server_url, options=capabilities_options)

time.sleep(2)
#if driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Allow access to files').is_displayed():
    #driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'ALLOW AND CONTINUE').click()
    #driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
    #                    ' new UiSelector().className("android.view.View").instance(4)').click()
    #driver.back()
#
#else: driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Home').click()

assert driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Home').is_displayed()

driver.quit()
appium_service.stop()

#self.driver.implicitly_wait(5)
#time.sleep(5)

#el1 = driver.find_element_by_id("in.amazon.mShop.android.shopping:id/sso_continue")
#el1.click()
#driver.find_element_by_id('in.amazon.mShop.android.shopping:id/sso_continue').click()
#driver.find_element(By.ID,'in.amazon.mShop.android.shopping:id/sso_continue').click()
#driver.find_element(AppiumBy.ACCESSIBILITY_ID('Continue in English')).click()
#driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR('new UiSelector().text("Skip sign in")')).click()
# driver.find_element_by_id('in.amazon.mShop.android.shopping:id/skip_sign_in_button').click()
# driver.find_element_by_id('in.amazon.mShop.android.shopping:id/rs_search_src_text').click()
#
# wait = WebDriverWait(driver,10)
# wait.until(EC.element_to_be_clickable((By.ID,'in.amazon.mShop.android.shopping:id/rs_search_src_text')))
# driver.find_element_by_id('in.amazon.mShop.android.shopping:id/rs_search_src_text').send_keys('Shoes')
# driver.press_keycode(66)
#time.sleep(5)
#driver.quit()
