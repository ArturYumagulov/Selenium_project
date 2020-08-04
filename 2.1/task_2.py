import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = "http://suninjuly.github.io/get_attribute.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


def sel_task(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        time.sleep(1)

        task_el = browser.find_element_by_css_selector("img")
        task = task_el.get_attribute('valuex')

        answer = browser.find_element_by_id("answer")
        answer.send_keys(calc(task))

        im_robot = browser.find_element_by_id('robotCheckbox')
        im_robot.click()

        robot_rule = browser.find_element_by_id('robotsRule')
        robot_rule.click()

        button = browser.find_element_by_css_selector('button')
        button.click()

    finally:
        time.sleep(10)
        browser.quit()


if __name__ == '__main__':
    sel_task(link)
