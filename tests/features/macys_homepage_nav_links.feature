Feature: Macys homepage navigation links
  Macy's homepage navigation links redirects a user to a proper category.
  Hover over navigation links displays subcategories

  Scenario Outline: Navigation link contains subcategories with items
    Given the User is on Macys homepage
    Then GA event page_view has a proper value
    When the User opens <nav_link_name>
    Then a URL contains a link text
    And result title contains a category name
    When the User clicks on <category_name>
    Then a number of subcategories is greater than 1

    Examples:
      | nav_link_name  |  category_name     |
      | Women          |  Juniors           |
      | Women          |  Beauty            |
      | Men            |  Services          |
      | Men            |  Electronics       |
      | Home           |  Mattresses        |
      | Home           |  Furniture         |

    Scenario: This test will fail
      Given the User is on Macys homepage
      When the User clicks on a fake button this test fail
