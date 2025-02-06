import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.select import Select

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

print(appium_service.is_running)
print(appium_service.is_listening)


appium_server_url = 'http://localhost:4723'
capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote(appium_server_url, options=capabilities_options)

driver.get("http://wikipedia.org")
print(driver.title)
#dropdown = driver.find_element(AppiumBy.ID,'searchLanguage') - not working
dropdown = driver.find_element(AppiumBy.CSS_SELECTOR,'#searchLanguage')
select = Select(dropdown)
select.select_by_value("uk")

options = driver.find_elements(AppiumBy.TAG_NAME,'option')

print(len(options))

for option in options:
    print("Text is : ",option.text," Lang is: ",option.get_attribute('Lang'))




time.sleep(2)
driver.quit()

appium_service.stop()

