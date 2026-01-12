Feature: POM Product Browsing

  Background:
    Given I have opened the browser

  @homepage
  Scenario Outline: Verify homepage access
    When I navigate to "<url>"
    Then the page title should contain "<expected_title>"

    Examples:
      | url                     | expected_title |
      | https://letcode.in/home | Products       |

  @product_detail @requires_pom_page
  Scenario Outline: Access product details
    Given I am on the POM homepage
    When I click on product with ID "<product_id>"
    Then I should be redirected to "<expected_path>"

    Examples:
      | product_id | expected_path |
      | 1          | /product/1    |
      | 2          | /product/2    |