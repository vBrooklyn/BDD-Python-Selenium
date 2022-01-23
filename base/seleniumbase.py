import allure
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from typing import List


class SeleniumBase:
    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(driver, 15, 0.3, ignored_exceptions=StaleElementReferenceException)

    @allure.step('Return a find by locator strategy')
    def __get_selenium_by(self, find_by: str) -> dict:
        '''Return a dictionary, where Keys are Strings representing a search locator strategies and Values are related By class values'''
        find_by = find_by.lower()
        locating = {'css': By.CSS_SELECTOR,
                    'xpath': By.XPATH,
                    'class_name': By.CLASS_NAME,
                    'id': By.ID,
                    'link_text': By.LINK_TEXT,
                    'name': By.NAME,
                    'partial_link_text': By.PARTIAL_LINK_TEXT,
                    'tag_name': By.TAG_NAME}
        return locating[find_by]

    @allure.step('Return a WebElement if it is visible on a page')
    def is_visible(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        '''Waiting on element and return WebElement if it is visible'''
        return self.__wait.until(ec.visibility_of_element_located((self.__get_selenium_by(find_by), locator)), locator_name)

    @allure.step('Return a WebElement if it is present on a page')
    def is_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        '''Waiting on element and return WebElement if it is present on DOM'''
        return self.__wait.until(ec.presence_of_element_located((self.__get_selenium_by(find_by), locator)), locator_name)

    @allure.step('Return WebElements if they are visible on a page')
    def are_visible(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        '''Waiting on elements and return WebElements if they are visible'''
        return self.__wait.until(ec.visibility_of_all_elements_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    @allure.step('Return WebElements if they are present on a page')
    def are_present(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        '''Waiting on elements and return WebElements if they are present on DOM'''
        return self.__wait.until(ec.presence_of_all_elements_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    @allure.step('Find a WebElement by text from a list of WebElements')
    def get_element_by_text(self, elements: List[WebElement], name: str) -> WebElement:
        '''The input should we a list of WebElements, from which we return a single WebElement found by it's name'''
        name = name.lower()
        return [element for element in elements if element.text.lower() == name][0]

    @allure.step('Delete an individual cookie')
    def delete_cookie(self, cookie_name: str) -> None:
        '''Delete a cookie by a name'''
        self.driver.delete_cookie(cookie_name)

    @allure.step('Wait for URL to contain these changes')
    def wait_for_url_contains(self, changes: str) -> None:
        self.__wait.until(ec.url_contains(changes))

    @allure.step('Wait for URL to become')
    def wait_for_url_change_to(self, string: str) -> None:
        """uses selenium's url_contains method to verify the url contains certain text in it"""
        self.__wait.until(ec.url_to_be(string))