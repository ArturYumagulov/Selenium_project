import pytest
from selenium import webdriver


link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser():
    print("\nstart browser for test")
    browser = webdriver.Chrome()
    return browser


class TestMAinPage1:
    def test_guest1(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_quest2(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
