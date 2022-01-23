import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

from abstract.selenium_listener import MyListener


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    # Use chrome or headless as an argument
    options.add_argument('headless')
    options.add_argument('--window-size=1650,900')
    #  User Agent Spoofing requires for headless mode to be able to navigate macys.com
    options.add_argument('user-agent=[Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36]')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options)
    driver = EventFiringWebDriver(driver, MyListener())
    yield driver


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'https://www.macys.com/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.quit()