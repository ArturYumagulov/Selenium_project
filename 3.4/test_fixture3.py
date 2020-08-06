import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="class")
def browser():
    print("\nstart browser")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser")
    browser.quit()


class TestMain:

    def test_reg1(self, browser):
        print("\nStart test1")
        browser.get(link)
        assert browser.find_element_by_css_selector("#login_link")
        print("\nFinish test1")

    def test_quest2(self, browser):
        print("\nStart test12")
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
        print("\nFinish test2")
