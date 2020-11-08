from selenium.webdriver.common.by import By
import pytest

from frame.base_page import BasePage
from frame.main import Main


class TestMain:
    def test_main(self):
        main = Main().gogo_market().goto_search()


def enhance(func):
    print('before')
    func()
    print('after')

def tem(func):
    def wrapper(*args, **kwargs): # 可以接任何的参数
        print('before')
        func(*args, **kwargs)
        print('after')
    return wrapper

@tem
def a(a1):
    # print('before')
    print('a')
    print(a1)
    # print('after')

def test_a():
    a(20)