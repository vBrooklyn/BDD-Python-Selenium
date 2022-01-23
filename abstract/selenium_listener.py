import time

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.events import AbstractEventListener

from base.seleniumbase import SeleniumBase


class MyListener(AbstractEventListener):

    def before_click(self, element, driver):
        '''Macy's website detects Selenium WebDriver as a bot,
        deleting a cookie ak_bmsc before a click prevents from Access Denied'''
        SeleniumBase(driver).delete_cookie('ak_bmsc')

    def after_click(self, element, driver):
        '''Macy's website detects Selenium WebDriver as a bot,
        deleting a cookie ak_bmsc after a click prevents from Access Denied'''
        SeleniumBase(driver).delete_cookie('ak_bmsc')

    @allure.step('Take a screenshot on exception')
    def on_exception(self, exception, driver):
        '''Take a screenshot if any WebDriver exception occurs'''
        print(exception)
        allure.attach(driver.get_screenshot_as_png(),
                      name='On_Exception_' + str(time.ctime()),
                      attachment_type=AttachmentType.PNG)
