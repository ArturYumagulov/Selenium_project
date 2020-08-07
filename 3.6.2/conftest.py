import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--bn', action='store', default=None,
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('bn')
    browser = None
    if browser_name == "ch":
        browser = webdriver.Chrome()
    elif browser_name == 'fx':
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    browser.quit()