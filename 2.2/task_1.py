import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"


def sel_task(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        num1 = browser.find_element_by_id('num1').text
        num2 = browser.find_element_by_id('num2').text
        ui = Select(browser.find_element_by_tag_name('select'))
        ui.select_by_value(str(int(num1) + int(num2)))
        button = browser.find_element_by_css_selector("button").click()

    finally:
        time.sleep(5)
        browser.quit()


if __name__ == '__main__':
    sel_task(link)