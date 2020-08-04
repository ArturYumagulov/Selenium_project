import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = "http://suninjuly.github.io/math.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


def sel_task(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        time.sleep(1)

        task = browser.find_element_by_xpath("html/body/div/form/div/label/span[@id='input_value']").text

        answer = browser.find_element_by_id("answer")
        answer.send_keys(calc(task))

        im_robot = browser.find_element_by_css_selector('[for="robotCheckbox"]')
        im_robot.click()

        robot_rule = browser.find_element_by_css_selector('[for="robotsRule"]')
        robot_rule.click()

        button = browser.find_element_by_css_selector('button')
        button.click()

    finally:
        time.sleep(3)
        browser.quit()


if __name__ == '__main__':
    sel_task(link)