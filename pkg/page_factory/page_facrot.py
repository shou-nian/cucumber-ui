from selenium import webdriver


class PageFactory:
    def __init__(self, browser: webdriver.Remote):
        self._browser = browser
        self._pages = {}

    def get_page(self, page_class):
        if page_class not in self._pages:
            self._pages[page_class] = page_class(self._browser)

        return self._pages[page_class]

    def reset(self):
        self._pages.clear()
