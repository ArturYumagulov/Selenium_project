import time
import math
from selenium import webdriver
import pytest

links = ["https://stepik.org/lesson/236895/step/1",
         "https://stepik.org/lesson/236896/step/1",
         "https://stepik.org/lesson/236897/step/1",
         "https://stepik.org/lesson/236898/step/1",
         "https://stepik.org/lesson/236899/step/1",
         "https://stepik.org/lesson/236903/step/1",
         "https://stepik.org/lesson/236904/step/1",
         "https://stepik.org/lesson/236905/step/1"]


string = ""


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.mark.parametrize('link', links)
class TestMain:
    def test(self, browser, link):
        browser.get(link)
        browser.implicitly_wait(20)
        browser.find_element_by_css_selector("textarea").send_keys(str(math.log(int(time.time()))))
        time.sleep(5)
        button = browser.find_element_by_class_name("submit-submission").click()
        time.sleep(3)
        text = browser.find_element_by_class_name("smart-hints__hint").text
        global string
        string += text
        print(string)

