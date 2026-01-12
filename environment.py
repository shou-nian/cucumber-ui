import inspect

from config import load_config
from pages import PomPage
from pkg import BrowserFactory, logger, PageFactory


def before_all(context):
    logger.name = __name__
    context.logger = logger
    context.logger.info(f"execute {inspect.currentframe().f_code.co_name}")

    browser_config = load_config()
    context.factory = BrowserFactory(browser_config)




def after_all(context):
    context.logger.info(f"execute {inspect.currentframe().f_code.co_name}")

    # context.factory.quit()


def before_tag(context, tag):
    context.logger.info(f"execute {inspect.currentframe().f_code.co_name}")

    if tag == "requires_pom_page":
        pom_page = context.pages.get_page(PomPage)
        pom_page.navigation("https://letcode.in/home")
        context.current_page = pom_page


def before_scenario(context, scenario):
    context.logger.info(f"execute {inspect.currentframe().f_code.co_name}")

    driver = context.factory.create_driver()
    context.pages = PageFactory(driver)


def after_scenario(context, scenario):
    context.logger.info(f"execute {inspect.currentframe().f_code.co_name}")

    context.current_page = None
    context.pages.reset()

    context.factory.quit()
