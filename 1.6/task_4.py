import time
from selenium import webdriver

link = "http://suninjuly.github.io/find_xpath_form"


def sel_task(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element_by_name('first_name')
        first_name.send_keys('Ivan')

        last_name = browser.find_element_by_name("last_name")
        last_name.send_keys('Ivanov')

        city = browser.find_element_by_name('firstname')
        city.send_keys("Moscow")

        country = browser.find_element_by_id("country")
        country.send_keys("Russia")

        submit = browser.find_element_by_xpath("html/body/div/form//button[text()='Submit']")
        submit.click()

    finally:
        time.sleep(10)
        browser.quit()


if __name__ == '__main__':
    sel_task(link)