from selenium import webdriver
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"

def selenium_task(link):
    try:
        browser = webdriver.Chrome()
        browser.get(url=link)

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
    selenium_task(link)