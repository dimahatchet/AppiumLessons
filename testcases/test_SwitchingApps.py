import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = dict(

    platformName="Android",
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='org.telegram.messenger',
    appActivity='org.telegram.ui.LaunchActivity'

)
appium_service = AppiumService()
appium_service.start()

appium_server_url = 'http://localhost:4723'

capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote(appium_server_url, options=capabilities_options)
driver.implicitly_wait(10)

driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Start Messaging")').click()
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Continue")').click()

driver.find_element(AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Country code').click()

#driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.View").instance(3)').click()
driver.press_keycode(10)
#driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.View").instance(8)').click()
driver.press_keycode(15)
#driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.View").instance(10)').click()
driver.press_keycode(7)
#driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Phone number').click()
#driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.View").instance(9)').click()
driver.press_keycode(16)
#driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.View").instance(6)').click()
driver.press_keycode(13)
#driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.View").instance(4)').click()
driver.press_keycode(11)
#driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.View").instance(8)').click()
driver.press_keycode(15)
#driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.View").instance(2)').click()
driver.press_keycode(9)
#driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.View").instance(9)').click()
driver.press_keycode(16)
#driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.View").instance(5)').click()
driver.press_keycode(12)
#driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.View").instance(1)').click()
driver.press_keycode(8)
#driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.View").instance(7)').click()
driver.press_keycode(14)
driver.implicitly_wait(10)
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Done")').click()
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Yes")').click()
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Continue")').click()
driver.find_element(AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()

#driver.find_element_by_id('net.one97.paytm:id/viewProceedClick').click()

#driver.find_element_by_id('com.android.permissioncontroller:id/permission_allow_button').click()
#time.sleep(2)
#driver.find_element_by_id('com.android.permissioncontroller:id/permission_allow_button').click()


#driver.find_element_by_xpath("//*[@text='Forgot Password?']").click()
time.sleep(2)
#driver.find_element_by_id('net.one97.paytm:id/viewProceedClick').click(
driver.activate_app('com.google.android.apps.messaging')
#driver.execute_script('mobile: startActivity', {'intent': 'com.google.android.apps.messaging/.main.MainActivity'})

driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Kyivstar")').click()
#messages = driver.find_elements(AppiumBy.ID,'message_text')
#print(messages)
messages2 = driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("message_text")')
print(messages2)
text3 = messages2[0].text
print(text3)
driver.back()
driver.terminate_app('com.google.android.apps.messaging')

time.sleep(10)
driver.quit()
