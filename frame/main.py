from selenium.webdriver.common.by import By

from frame.base_page import BasePage
from frame.market import Market


class Main(BasePage):
    def gogo_market(self):
        self.find(By.XPATH, "//*[resource-id='']").click()
        self.find(By.XPATH, "//*[@resource=id='android:id/tabs']//*[@text='行情']").click()
        return Market(self.driver)