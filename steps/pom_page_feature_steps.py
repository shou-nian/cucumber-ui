from behave import use_step_matcher, given, when, then

from pages import PomPage

use_step_matcher("re")


@given("I open browser visit pom page")
def step_open_browser(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when('I using the url: "(?P<pom_page_url>.+)" navigation to pom page')
def step_navigation_to_pom_page(context, pom_page_url):
    """
    :type context: behave.runner.Context
    :type pom_page_url: str
    """
    pom_page: PomPage = context.pages.get_page(PomPage)
    pom_page.navigation_pom_page(pom_page_url)

    context.current_page = pom_page


@then('Page title can should be "(?P<page_title>.+)"')
def step_check_page_title(context, page_title):
    """
    :type context: behave.runner.Context
    :type page_title: str
    """
    assert page_title == context.current_page.page_title
