from config import load_config
from pkg import BrowserFactory, logger, PageFactory


def before_all(context):
    browser_config = load_config()
    context.factory = BrowserFactory(browser_config)

    logger.name = __name__
    context.logger = logger


def after_all(context):
    context.factory.quit()


def before_scenario(context, scenario):
    driver = context.factory.create_driver()
    context.pages = PageFactory(driver)


def after_scenario(context, scenario):
    context.pages.reset()
