import math
from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_link_text"


def sel_task(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        time.sleep(3)
        links = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
        links.click()

        first_name = browser.find_element_by_name('first_name')
        first_name.send_keys('Ivan')

        last_name = browser.find_element_by_name("last_name")
        last_name.send_keys('Ivanov')

        city = browser.find_element_by_name('firstname')
        city.send_keys("Moscow")

        country = browser.find_element_by_id("country")
        country.send_keys("Russia")

        submit = browser.find_element_by_css_selector("button.btn")
        submit.click()
    finally:
        time.sleep(10)
        browser.quit()


if __name__ == '__main__':
    sel_task(link)
