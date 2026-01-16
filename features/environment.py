import functools
import inspect
import time

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

    _cls = _mapping.get(page_name, None)
    if _cls is None:
        raise ValueError(f'Page {page_name} not supported')

    return _cls


fixture_registry = {
    "fixture.browser": browser,
    "fixture.pages": pages,
}


def auto_screenshot_with_failed(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        context, step = args
        if step.status == 'failed':
            context.logger.error(f"test step failed: {step.keyword} {step.name}, start auto screenshot...")
            context.browser.save_screenshot(
                f"{time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())}.png"
            )

        func(*args, **kwargs)

    return wrapper


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


def before_step(context, step):
    context.logger.info(f"execute {inspect.currentframe().f_code.co_name}")


@auto_screenshot_with_failed
def after_step(context, step):
    context.logger.info(f"execute {inspect.currentframe().f_code.co_name}")
