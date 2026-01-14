from behave import use_step_matcher, given, when, then

from pages import PomPage

use_step_matcher("re")


@given("I have opened the browser")
def step_open_browser(context):
    """
    :type context: behave.runner.Context
    """
    context.logger.info("execute background.")


@when('I navigate to pom page')
def step_navigate_to_pom_page(context):
    """
    :type context: behave.runner.Context
    """
    pom_page: PomPage = context.pages.get_page(PomPage)
    context.logger.info("navigate to pom page")
    pom_page.navigation()

    context.current_page = pom_page


@then('the page title should contain "(?P<expected_title>.+)"')
def step_check_pom_page_title(context, expected_title):
    """
    :type context: behave.runner.Context
    :type expected_title: str
    """
    context.logger.info(
        f"expected title is {expected_title}, got {context.current_page.get_page_title}"
    )
    assert context.current_page.get_page_title == expected_title


@given("I am on the POM homepage")
def step_on_pom_page(context):
    """
    :type context: behave.runner.Context
    """
    context.logger.info("on the POM homepage")


@when('I click on product with ID "(?P<product_id>.+)"')
def step_click_product_with_id(context, product_id):
    """
    :type context: behave.runner.Context
    :type product_id: str
    """
    context.logger.info(f"click on product with ID {product_id}")
    context.current_page.click_product_with_id(product_id)


@then('I should be redirected to "(?P<expected_path>.+)"')
def step_check_redirect_url(context, expected_path):
    """
    :type context: behave.runner.Context
    :type expected_path: str
    """
    page_path = context.current_page.get_page_path
    context.logger.info(
        f"expected path is {expected_path}, got {page_path[len(page_path) - len(expected_path):]}"
    )
    assert page_path[len(page_path) - len(expected_path):] == expected_path
