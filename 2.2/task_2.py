import time
import math
from selenium import webdriver

link = "http://suninjuly.github.io/execute_script.html"


def sel_task(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        x = browser.find_element_by_id("input_value").text
        value = str(math.log(abs(12 * math.sin(int(x)))))
        answer = browser.find_element_by_id('answer').send_keys(value)
        robot = browser.find_element_by_css_selector("[for='robotCheckbox']").click()
        button = browser.find_element_by_tag_name("button")
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        robots = browser.find_element_by_css_selector("[for='robotsRule']").click()
        click = button.click()

    finally:
        time.sleep(5)
        browser.quit()


if __name__ == '__main__':
    sel_task(link)
