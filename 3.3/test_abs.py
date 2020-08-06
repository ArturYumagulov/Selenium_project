from selenium import webdriver


class Registration:
    def __init__(self):
        self.browser = webdriver.Chrome()

    def start(self, link):
        try:
            self.browser.get(link)
            self.browser.implicitly_wait(5)
            first_name = self.browser.find_element_by_xpath(
                "html/body/div/form/div[@class='first_block']/div[@class='form-group first_class']/input")\
                .send_keys("first_name")
            last_name = self.browser.find_element_by_xpath("html/body/div/form/div[@class='first_block']/"
                                                           "div[@class='form-group second_class']/input")\
                .send_keys("last_name")
            email = self.browser.find_element_by_xpath("html/body/div/form/div[@class='first_block']/"
                                                       "div[@class='form-group third_class']/input")\
                .send_keys("email")
            submit = self.browser.find_element_by_css_selector('button.btn').click()
            text = self.browser.find_element_by_css_selector('h1').text

        finally:
            self.browser.quit()


class Test:
    def test_reg1(self):
        x = Registration()
        assert x.start("http://suninjuly.github.io/registration1.html") == None, "Should be absolute value od number"

    def test_req2(self):
        x = Registration()
        assert x.start("http://suninjuly.github.io/registration2.html") == None, "Should be absolute value od number"
