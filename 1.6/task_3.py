import time
from selenium import webdriver

link = "http://suninjuly.github.io/huge_form.html"


def sel_task(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        # time.sleep(5)
        forms = browser.find_elements_by_css_selector("input")
        for i in forms:
            i.send_keys("test")
        submit = browser.find_element_by_css_selector('button.btn')
        submit.click()
    finally:
        time.sleep(10)
        browser.quit()


if __name__ == '__main__':
    sel_task(link)