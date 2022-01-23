import allure

from base.seleniumbase import SeleniumBase


class GoogleAnalytics(SeleniumBase):
    @allure.step('Get Data Layer object')
    def get_datalayer(self) -> list:
        '''Return JS dataLayer object'''
        return self.driver.execute_script('return dataLayer;')

    @allure.step('Get Data Layer events')
    def get_datalayer_events(self, data_layer: list) -> list:
        '''Parse dataLayer object for events'''
        return [data for data in data_layer if 'event' in data]

    @allure.step('Get specific data layer action')
    def get_specific_datalayer_events(self, data_layer: list, specific_event: str) -> list:
        data_layer_events = self.get_datalayer_events(data_layer)
        return [event for event in data_layer_events if specific_event in event]