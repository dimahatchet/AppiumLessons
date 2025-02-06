import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = dict(

    platformName="Android",
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.android.chrome',
    appActivity= 'org.chromium.chrome.browser.ChromeTabbedActivity'

)
appium_service = AppiumService()
appium_service.start()

appium_server_url = 'http://localhost:4723'



capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote(appium_server_url, options=capabilities_options)
driver.implicitly_wait(10)

#driver.find_element(AppiumBy.ID,"com.android.chrome:id/signin_fre_continue_button").click()
driver.find_element(AppiumBy.ID,"com.android.chrome:id/signin_fre_dismiss_button").click()
#driver.find_element(AppiumBy.ID,"com.android.chrome:id/button_secondary").click()
driver.find_element(AppiumBy.ID,"com.android.chrome:id/ack_button").click()

#driver.get('http://google.com')
time.sleep(2)
contexts = driver.contexts
for context in contexts:
     print(context)

#driver.switch_to.context('WEBVIEW_chrome')

webview = driver.contexts[1]

driver.switch_to.context(webview)

driver.find_element(AppiumBy.XPATH,"//*[@name='q']").send_keys("Hello Appium !!!")

time.sleep(2)
driver.quit()