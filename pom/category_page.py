from typing import List

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from base.seleniumbase import SeleniumBase


class CategoryPage(SeleniumBase):
    __category_name_title = 'h1[class=result-category-name]'
    __categories = 'div[class=accordion]'

    @allure.step('Return a category name title WebElement')
    def get_category_name_title(self) -> WebElement:
        return self.is_visible('css', self.__category_name_title, 'A title for category name')

    @allure.step('Return all categories WebElements')
    def get_all_categories(self) -> List[WebElement]:
        return self.are_visible('css', self.__categories, 'All Categories')

    @allure.step('Find nav link WebElement by a text')
    def get_category_by_name(self, name: str) -> WebElement:
        '''Return a nav link WebElement, the input is a link's name'''
        elements = self.get_all_categories()
        return self.get_element_by_text(elements, name)

    @allure.step('Return all subcategories of a giving category')
    def get_subcategories(self, element) -> WebElement:
        return element.find_elements(By.TAG_NAME, 'li')
