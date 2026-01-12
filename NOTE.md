# .feature文件

- 1.文件模板
    ```
  # login.feature

  Feature: User login

  Background:
    Give I have registed account

  @smoke
  Scenario Outline: Use correct username and password login
    Give I loaded the API client
    When I input "<username>" and "<password>" on the login api payload
    And Send the request to service
    Then The request response code should be "<response_code>"
    And The request response body can should be "<expected_body>"

    Examples:
      | username | password    | response_code | expected_body                       |
      | zhangsan | zhangsan123 | 200           | {"data": {"user_name": "zhangsan"}} |
      | lisi     | lisi123     | 200           | {"data": {"user_name": "lisi"}}     |
  
  @edge
  Scenario Outline: Use wrong username and password login
    Give I loaded the API client
    When I input "<username>" and "<password>" on the login api payload
    And Send the request to service
    Then The request response code should be "<response_code>"
    And The request response message can should be contain "<error_msg>"

    Examples:
      | username | password    | response_code | error_msg                  |
      |          | zhangsan123 | 400           | username or password error |
      | lisi     |             | 400           | username or password error |
  
  @requires_login
  ```
- 2
