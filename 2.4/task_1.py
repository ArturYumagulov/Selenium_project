import time
from selenium import webdriver

link = "http://suninjuly.github.io/wait1.html"


def sel_task(link):
    try:
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(link)
        button = browser.find_element_by_css_selector('button').click()
        message = browser.find_element_by_id('verify_message').text
        assert message == "Verification was successful!"
    finally:
        browser.quit()


if __name__ == '__main__':
    sel_task(link)