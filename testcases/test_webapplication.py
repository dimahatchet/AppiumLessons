import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = dict(

    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    language='en',
    locale='US',
    browserName='Chrome'

)

appium_service = AppiumService()
appium_service.start()

appium_server_url = 'http://localhost:4723'
capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote(appium_server_url, options=capabilities_options)

driver.get("http://google.com")
print(driver.title)
driver.find_element(AppiumBy.XPATH,"//*[@name='q']").send_keys("Hello Appium !!!")

#driver.find_element(AppiumBy.CSS_SELECTOR,"//*[@name='q']").send_keys("Hello Appium !!!")
#driver.find_element(AppiumBy.NAME, "q").send_keys("Hello")

time.sleep(2)
driver.quit()

appium_service.stop()