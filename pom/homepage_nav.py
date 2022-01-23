from typing import List

import allure
from selenium.webdriver.remote.webelement import WebElement

from base.seleniumbase import SeleniumBase


class HomepageNav(SeleniumBase):

    __nav_links: str = '#mainNavigationFobs>li'
    __fake_button = '#fake_button'

    @allure.step('Return nav links WebElements')
    def get_nav_links(self) -> List[WebElement]:
        '''Return WebElements for nav links'''
        return self.are_visible('css', self.__nav_links, 'Header Navigation Links')

    @allure.step('Find nav link WebElement by a text')
    def get_nav_link_by_name(self, name: str) -> WebElement:
        '''Return a nav link WebElement, the input is a link's name'''
        elements = self.get_nav_links()
        return self.get_element_by_text(elements, name)

    @allure.step('This is a fake button')
    def get_fake_button(self):
        return self.is_visible('css', self.__fake_button, 'This is a fake locator')