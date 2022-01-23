import pytest
from pytest_bdd import scenario, given, then, when, parsers
from pytest_check import check

from base.google_analytics import GoogleAnalytics
from pom.category_page import CategoryPage
from pom.homepage_nav import HomepageNav


@pytest.fixture
def homepage_nav(get_webdriver):
    return HomepageNav(get_webdriver)


@pytest.fixture
def category_page(get_webdriver):
    return CategoryPage(get_webdriver)


@pytest.fixture
def google_analytics(get_webdriver):
    return GoogleAnalytics(get_webdriver)


@pytest.fixture
def link_name() -> list:
    return []


@pytest.fixture
def webelement() -> list:
    return []


@pytest.mark.usefixtures('setup')
@scenario('../features/macys_homepage_nav_links.feature',
          'Navigation link contains subcategories with items')
def test_navigation_link_contains_subcategories_with_items():
    """A user opens subcategories through navigation links"""
    pass


@pytest.mark.usefixtures('setup')
@scenario('../features/macys_homepage_nav_links.feature',
          'This test will fail')
def test_fail_test():
    """This test will fail"""
    pass


@given('the User is on Macys homepage')
def macys_homepage(homepage_nav):
    """"The User is on Macy's homepage"""
    homepage_nav.wait_for_url_change_to('https://www.macys.com/')


@when('the User clicks on a fake button this test fail')
def user_clicks_on_fake_button(homepage_nav):
    homepage_nav.get_fake_button().click()


@then(parsers.parse('GA event {page_view:w} has a proper value'))
def assert_ga_event_has_proper_value(google_analytics, page_view):
    '''Assert that GA event presents in a dataLayer object'''
    data_layer = google_analytics.get_datalayer()
    page_view_events = google_analytics.get_specific_datalayer_events(data_layer, page_view)
    page_view = page_view_events[-1]
    page_view = page_view[-1].get('dimension13')
    with check:
        assert 'home page' == page_view, 'Incorrect value in Page View GA event'


@when(parsers.parse('the User opens {nav_link_name:w}'))
def the_user_opens_nav_link(homepage_nav, nav_link_name, link_name, google_analytics):
    """The user clicks on a navigation link"""
    homepage_nav.get_nav_link_by_name(nav_link_name).click()
    link_name.append(nav_link_name)


@then('a URL contains a link text')
def url_contains_link_text(homepage_nav, link_name):
    """Validate that a navigation link text appears on new URL"""
    homepage_nav.wait_for_url_contains(link_name[-1].lower())


@then('result title contains a category name')
def result_title_contains_category_name(category_page, link_name):
    expected = link_name[-1]
    actual = category_page.get_category_name_title().text
    with check:
        assert expected == actual, f'Title does not match selected nav link {expected}, instead {actual}'


@when(parsers.parse('the User clicks on {category_name:w}'))
def the_user_opens_nav_link(category_page, category_name, webelement):
    """The user clicks on a navigation link"""
    webelement.append(category_page.get_category_by_name(category_name))
    webelement[-1].click()


@then(parsers.parse('a number of subcategories is greater than {expected_number_of_subcategories:d}'))
def number_of_subcategories_greater_than_expected(category_page, expected_number_of_subcategories, webelement):
    actual_number_of_subcategories = category_page.get_subcategories(webelement[-1])
    with check:
        assert expected_number_of_subcategories < len(actual_number_of_subcategories), f'Actual number of subcategories should be greater than {expected_number_of_subcategories}'