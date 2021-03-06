from selenium.webdriver.common.by import By

from frame.base_page import BasePage
from frame.search import Search


class Market(BasePage):
    def goto_search(self):
        self.find(By.XPATH, "").click()
        return Search(self.driver)