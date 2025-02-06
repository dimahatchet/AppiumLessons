from selenium.webdriver import ActionChains


class ScrollUtil:

    @staticmethod
    def scrollToTextByAndroidUIAutomator(text,driver):
        driver.find_element_by_android_uiautomator("new UiScrollable(new UiSelector().scrollable(true).instance("
                                                   "0)).scrollIntoView(new UiSelector().textContains(\""+text+"\").instance(0))").click()



    @staticmethod
    def swipeUp(howManySwipes,driver):
        for i in range(1,howManySwipes+1):
            driver.swipe(514, 600, 514, 200, 1000)

    @staticmethod
    def swipeUpNew(howManySwipes, driver):
        action = ActionChains(driver)
        for i in range(1, howManySwipes + 1):
            action.w3c_actions.pointer_action.move_to_location(514, 600)
            action.w3c_actions.pointer_action.pointer_down()
            action.w3c_actions.pointer_action.move_to_location(514, 200)
            action.w3c_actions.pointer_action.pointer_up()
            action.perform()
            action.reset_actions()

    @staticmethod
    def swipeDown(howManySwipes,driver):
        for i in range(1, howManySwipes + 1):
            driver.swipe(514, 500, 514, 800, 1000)

    @staticmethod
    def swipeDownNew(howManySwipes, driver):
        action = ActionChains(driver)
        for i in range(1, howManySwipes + 1):
            action.w3c_actions.pointer_action.move_to_location(514, 500)
            action.w3c_actions.pointer_action.pointer_down()
            action.w3c_actions.pointer_action.move_to_location(514, 800)
            action.w3c_actions.pointer_action.pointer_up()
            action.perform()
            action.reset_actions()

    @staticmethod
    def swipeLeft(howManySwipes,driver):
        for i in range(1, howManySwipes + 1):
            driver.swipe(900, 600, 200, 600, 1000)

    @staticmethod
    def swipeLeftNew(howManySwipes, driver):
        action = ActionChains(driver)
        for i in range(1, howManySwipes + 1):
            action.w3c_actions.pointer_action.move_to_location(900, 600)
            action.w3c_actions.pointer_action.pointer_down()
            action.w3c_actions.pointer_action.move_to_location(200, 600)
            action.w3c_actions.pointer_action.pointer_up()
            action.perform()
            action.reset_actions()



    @staticmethod
    def swipeRight(howManySwipes,driver):
        for i in range(1, howManySwipes + 1):
            driver.swipe(200, 600, 900, 600, 1000)

    @staticmethod
    def swipeRightNew(howManySwipes, driver):
        action = ActionChains(driver)
        for i in range(1, howManySwipes + 1):
            action.w3c_actions.pointer_action.move_to_location(200, 600)
            action.w3c_actions.pointer_action.pointer_down()
            action.w3c_actions.pointer_action.move_to_location(900, 600)
            action.w3c_actions.pointer_action.pointer_up()
            action.perform()
            action.reset_actions()