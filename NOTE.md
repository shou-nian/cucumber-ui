# .feature文件

- 1.文件模板

```gherkin
# passport.feature

Feature: User login

  Background:
    Given I have registed account

  @smoke
  Scenario Outline: Use correct username and password login
    Given I loaded the API client
    When I input "<username>" and "<password>" on the login api payload
    And Send the request to service
    Then The request response code should be "<response_code>"
    And The request response body should be "<expected_body>"

    Examples:
      | username | password    | response_code | expected_body                       |
      | zhangsan | zhangsan123 | 200           | {"data": {"user_name": "zhangsan"}} |
      | lisi     | lisi123     | 200           | {"data": {"user_name": "lisi"}}     |

  @edge
  Scenario Outline: Use wrong username and password login
    Given I loaded the API client
    When I input "<username>" and "<password>" on the login api payload
    And Send the request to service
    Then The request response code should be "<response_code>"
    And The request response message should be contain "<error_msg>"
    But xxx

    Examples:
      | username | password    | response_code | error_msg                  |
      |          | zhangsan123 | 400           | username or password error |
      | lisi     |             | 400           | username or password error |

  @requires_login @smoke
  Scenario Outline: Logout
    Given I am logined
    When I send a logout request to the api service
    Then The request response code should be "<response_code>"
    And Response body should be "<response_body>"
    And Clear my login status

    Examples:
      | response_code | response_body      |
      | 200           | logout successful. |
  ```

- 3.environment.py

```python
# 在某些事件之前或之后执行的hooks func
def before_all(context):
    """
    Running with before all script
    """


def after_all(context):
    """
    Running with after all script
    """


def before_feature(context, feature):
    """
    Running with before feature
    """


def after_feature(context, feature):
    """
    Running with after feature
    """


def before_tag(context, tag):
    """
    Running with before tag
    """


def after_tag(context):
    """
    Running with after tag
    """


def before_scenario(context, scenario):
    """
    Running with before scenario
    """


def after_scenario(context, scenario):
    """
    Running with after scenario
    """


def before_step(context, step):
    """
    Running with before step
    """


def after_step(context, step):
    """
    Running with after step
    """


# 使用fixture
from behave.fixture import fixture, use_fixture_by_tag


@fixture
def fixture_func(context):
    """
    # Example1:
        driver = webdriver.Chrome()
        yield driver
        driver.close()
    
    # Example2:
        client = requests.Session()
        yield client
        client.close()
    """


fixture_registry = {
    "fixture.name": fixture_func,
}


# use the fixture func
def before_func(context):
    use_fixture_by_tag(context.tag, context, fixture_registry)
```

- 2.behave.ini

```ini

```

- 3.关键字说明

```markdown
Feature：功能名称

Background：背景，一般作为一个feature文件中所有场景的前置

Scenario | Scenario Outline：场景和场景大纲（带参数的场景）

Given：假设，所依赖的系统、服务、状态说明。

When：当做某个操作时

Then：对应操作将系统状态改变，所期望的状态

And | But：关联性步骤

Examples：参数
```

- 4.hooks执行顺序

```markdown
before_all -> before_feature -> before_tag -> after_tag ->
before_scenario -> before_step -> after_step -> after_scenario ->
after_feature -> after_all
```

- 5.report output

```python

```

- Other

```markdown
Seriously, Don’t Test the User Interface

Warning
While you can use behave to drive the “user interface” (UI) or front-end, interacting with the model layer or the
business logic, e.g. by using a REST API, is often the better choice.
And keep in mind, BDD advises your to test WHAT your application should do and not HOW it is done.
```

```html
<a href="https://jenisys.github.io/behave.example/">教程</a>
```