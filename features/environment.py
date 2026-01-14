import inspect

from behave.fixture import fixture, use_fixture_by_tag

from config import load_config
from pages import PomPage
from pkg import BrowserFactory, logger, PageFactory


@fixture
def browser(context):
    browser_config = load_config()
    context.factory = BrowserFactory(browser_config)
    context.browser = context.factory.create_browser()
    yield context.browser
    context.factory.quit()


@fixture
def pages(context):
    context.pages = PageFactory(context.browser)
    yield context.pages
    context.pages.reset()


def page_class_mapping(page_name: str):
    _mapping = dict(
        pom=PomPage,
    )

    return _mapping.get(page_name, None)


fixture_registry = {
    "fixture.browser": browser,
    "fixture.pages": pages,
}


def before_all(context):
    logger.name = __name__
    context.logger = logger
    context.logger.info(f"execute {inspect.currentframe().f_code.co_name}")


def after_all(context):
    context.logger.info(f"execute {inspect.currentframe().f_code.co_name}")


def before_feature(context, feature):
    context.logger.info(f"execute {inspect.currentframe().f_code.co_name}")


def after_feature(context, feature):
    context.logger.info(f"execute {inspect.currentframe().f_code.co_name}")


def before_tag(context, tag):
    context.logger.info(f"execute {inspect.currentframe().f_code.co_name}")

    if tag.startswith("fixture."):
        use_fixture_by_tag(tag, context, fixture_registry)

    if tag.startswith("requires"):
        tag_list = tag.split(".")
        # requires page
        if tag_list[1] == "page":
            _page_class = page_class_mapping(tag_list[-1])
            page = context.pages.get_page(_page_class)
            page.navigation()
            context.current_page = page

        # other requires


def after_tag(context, tag):
    context.logger.info(f"execute {inspect.currentframe().f_code.co_name}")


def before_scenario(context, scenario):
    context.logger.info(f"execute {inspect.currentframe().f_code.co_name}")


def after_scenario(context, scenario):
    context.logger.info(f"execute {inspect.currentframe().f_code.co_name}")

    context.current_page = None
