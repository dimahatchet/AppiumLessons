import allure
import pytest
from allure_commons.types import AttachmentType
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_make_report(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture(scope="function")
def appium_driver():
    desired_caps = dict(

        platformName="Android",
        automationName='uiautomator2',
        deviceName='Android',
        appPackage='com.google.android.calculator',
        appActivity='com.android.calculator2.Calculator',
        language='en',
        locale='US',
        noReset = True

    )

    #appium_service = AppiumService()
    #appium_service.start()

    appium_server_url = 'http://localhost:4723'
    capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)

    global driver
    driver = webdriver.Remote(appium_server_url, options=capabilities_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


# @pytest.fixture(scope="function")
# def appium_driver():
#     #global appium_service
#     #appium_service = AppiumService()
#     #appium_service.start()
#
#     desired_caps = {}
#     desired_caps['platformName'] = 'Android'
#     desired_caps['deviceName'] = 'Android'
#     desired_caps['appPackage'] = 'com.goibibo'
#     desired_caps['appActivity'] = '.common.HomeActivity'
#     desired_caps['noReset'] = True
#     global driver
#     driver = webdriver.Remote('http://localhost:4724/wd/hub', desired_caps)
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()
#     #appium_service.stop()


@pytest.fixture()
def screen_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
#
# @pytest.fixture(params=["device1", "device2"], scope="function")
# def appium_driver(request):
#     if request.param == "device1":
#         desired_caps = {}
#         desired_caps['platformName'] = 'Android'
#         desired_caps['deviceName'] = 'Android'
#         desired_caps['udid'] = 'emulator-5554'
#         desired_caps['browserName'] = 'Chrome'
#         driver = webdriver.Remote('http://localhost:4444/wd/hub', desired_caps)
#     if request.param == "device2":
#         desired_caps = {}
#         desired_caps['platformName'] = 'Android'
#         desired_caps['deviceName'] = 'Android'
#         desired_caps['udid'] = '8e006adb'
#         desired_caps['browserName'] = 'Chrome'
#         driver = webdriver.Remote('http://localhost:4444/wd/hub', desired_caps)
#
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()
#     appium_service.stop()