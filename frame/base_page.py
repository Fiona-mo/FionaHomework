from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _black_list = [By.XPATH, "xxx"]
    _max_num = 3
    _error_num = 0
    def __init__(self, drvier:WebDriver=None):
        """
        initional
        """

        if drvier is None:
            caps = {}
            caps["platformName"] = "android"
            caps["appPackage"] = "com.xueqiu.android"
            caps["appActivity"] = ".view.WelcomActivityAlias"
            caps["noReset"] = "true"
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(20)
        else:
            self.driver = drvier

    def find(self, by, locator=None):
        try:
            if locator is None:
                result = self.driver.find_element(*by)
            else:
                result = self.driver.find_element(by, locator)
            self._error_num = 0
            return result
        except Exception as e:
            if self._error_num > self._max_num:
                raise e
            self._error_num += 1
            for black_ele in self._black_list:
                ele = self.driver.find_elements(*ele)
                if len(ele) > 0:
                    ele[0].click()
                    # 如果处理黑名单之后，再次查找元素
                    ## code
                    return self.find(by, locator)
            raise e