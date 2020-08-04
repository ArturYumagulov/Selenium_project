import time
from selenium import webdriver

old_link = "http://suninjuly.github.io/registration1.html"  # старая ссылка
update_link = "http://suninjuly.github.io/registration1.html"  # обновленная ссылка
error_link = "http://suninjuly.github.io/registration2.html"  # ссылка с ошибкой


def sel_task(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        time.sleep(1)

        first_name = browser.find_element_by_xpath("html/body/div/form/div[@class='first_block']/"
                                                   "div[@class='form-group first_class']/input")
        first_name.send_keys("first_name")
        time.sleep(1)

        last_name = browser.find_element_by_xpath("html/body/div/form/div[@class='first_block']/"
                                                  "div[@class='form-group second_class']/input")
        last_name.send_keys("last_name")
        time.sleep(1)

        email = browser.find_element_by_xpath("html/body/div/form/div[@class='first_block']/"
                                              "div[@class='form-group third_class']/input")
        email.send_keys("email")
        time.sleep(1)

        submit = browser.find_element_by_css_selector('button.btn')
        submit.click()
        time.sleep(1)
        text = browser.find_element_by_css_selector('h1').text
        assert text == "Congratulations! You have successfully registered!"
    finally:
        time.sleep(3)
        browser.quit()


if __name__ == '__main__':
    sel_task(update_link)
    # sel_task(error_link)
    # sel_task(old_link)
