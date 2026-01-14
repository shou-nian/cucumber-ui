Feature: POM Product Browsing

  Background:
    Given I have opened the browser

  @fixture.browser @fixture.pages
  Scenario Outline: Verify homepage access
    When I navigate to pom page
    Then the page title should contain "<expected_title>"

    Examples:
      | expected_title |
      | Products       |

  @fixture.browser @fixture.pages @requires.page.pom
  Scenario Outline: Access product details
    Given I am on the POM homepage
    When I click on product with ID "<product_id>"
    Then I should be redirected to "<expected_path>"

    Examples:
      | product_id | expected_path |
      | 1          | /product/1    |
      | 2          | /product/2    |