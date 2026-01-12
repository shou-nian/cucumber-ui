from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base import BasePage


class PomPage(BasePage):
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver

        self._page_title_locator = (By.CSS_SELECTOR, "h2.title")
        self._product_locator = (By.CSS_SELECTOR, ".columns div:nth-child(%s) > .card")

    def navigation(self, page_url: str):
        self.driver.get(page_url)

    @property
    def get_page_title(self) -> str:
        return self.driver.find_element(*self._page_title_locator).text

    @property
    def get_page_path(self) -> str:
        return self.driver.current_url

    def click_product_with_id(self, product_id: str):
        _by, _selector = self._product_locator

        return self.driver.find_element(_by, _selector % product_id).click()
