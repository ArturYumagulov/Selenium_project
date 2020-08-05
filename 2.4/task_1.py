from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/explicit_wait2.html"


def sel_task(link):
    try:
        browser = webdriver.Chrome()

        browser.get(link)
        price = WebDriverWait(browser, 12).until(expected_conditions.text_to_be_present_in_element((By.ID, 'price'),
                                                                                                   '100'))
        button = browser.find_element_by_id('book').click()

        digit = browser.find_element_by_id("input_value").text
        answer = browser.find_element_by_id('answer').send_keys(str(math.log(abs(12 * math.sin(int(digit))))))
        submit = browser.find_element_by_id('solve').click()
    finally:
        time.sleep(10)
        browser.quit()


if __name__ == '__main__':
    sel_task(link)