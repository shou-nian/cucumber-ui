import abc


class BasePage(abc.ABC):
    @abc.abstractmethod
    def navigation(self, url):
        """
        navigation to the url page
        """

    @abc.abstractmethod
    def get_page_title(self) -> str:
        """

        :return: the current page title
        """

    @abc.abstractmethod
    def get_page_path(self) -> str:
        """

        :return: the current page path
        """
