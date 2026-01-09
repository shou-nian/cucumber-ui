Feature:

  Scenario Outline:
    Given I open browser visit pom page
    When I using the url: "<pom_page_url>" navigation to pom page
    Then Page title can should be "<page_title>"
    Examples:
      | pom_page_url            | page_title |
      | https://letcode.in/home | Products   |