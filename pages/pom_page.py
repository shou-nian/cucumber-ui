from selenium import webdriver
from selenium.webdriver.common.by import By


class PomPage:
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver

        self._page_title_locator = (By.CSS_SELECTOR, "h2.title")

    def navigation_pom_page(self, page_url: str):
        self.driver.get(page_url)

    def page_title(self) -> str:
        return self.driver.find_element(*self._page_title_locator).text
