from enum import Enum
from typing import Any, Dict, Optional

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from pkg.utils import logger

logger.name = __name__


class BrowserType(Enum):
    CHROME: str = "chrome"
    FIREFOX: str = "firefox"


class BrowserFactory:
    def __init__(self, config: Dict[str, Any]) -> None:
        self._config = config
        self._driver = None

    def create_driver(self, browser_type: Optional[str] = None) -> webdriver.Remote:
        browser = browser_type or self._config.get("default_browser", "chrome")
        browser = browser.lower()

        try:
            if browser == BrowserType.CHROME.value:
                self._driver = self._create_chrome_driver()
            elif browser == BrowserType.FIREFOX.value:
                self._driver = self._create_firefox_driver()
            else:
                raise ValueError(f"不支持的浏览器类型: {browser}")

            self._setup_driver_options()
            logger.info(f"成功创建 {browser.upper()} 浏览器驱动")
            return self._driver


        except Exception as e:
            logger.error(f"创建浏览器驱动失败: {e}")
            raise

    def _create_chrome_driver(self) -> webdriver.Chrome:
        options = webdriver.ChromeOptions()

        chrome_config = self._config.get("chrome", {})

        # 设置headless模式
        if chrome_config.get("headless", False):
            options.add_argument("--headless=new")

        # 设置其他参数
        for arg in chrome_config.get("arguments", []):
            options.add_argument(arg)

        # 设置实验性选项
        for key, value in chrome_config.get("experimental_options", {}).items():
            options.add_experimental_option(key, value)

        # 禁用自动化控制提示
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

        # 处理驱动下载及路径配置
        if self._config.get("webdriver_manager", True):
            service = ChromeService(ChromeDriverManager().install())
        else:
            driver_path = chrome_config.get("driver_path", None)
            service = ChromeService(executable_path=driver_path) if driver_path else None

        return webdriver.Chrome(service=service, options=options)

    def _create_firefox_driver(self) -> webdriver.Firefox:
        """创建Firefox浏览器驱动"""
        options = webdriver.FirefoxOptions()
        firefox_config = self._config.get("firefox", {})

        if firefox_config.get("headless", False):
            options.add_argument("--headless")

        for arg in firefox_config.get("arguments", []):
            options.add_argument(arg)

        # Firefox特定的首选项
        for key, value in firefox_config.get("preferences", {}).items():
            options.set_preference(key, value)

        if self._config.get("webdriver_manager", True):
            service = FirefoxService(GeckoDriverManager().install())
        else:
            driver_path = firefox_config.get("driver_path")
            service = FirefoxService(executable_path=driver_path) if driver_path else None

        return webdriver.Firefox(service=service, options=options)

    def _setup_driver_options(self):
        """设置驱动通用选项"""
        if not self._driver:
            return

        # 设置隐式等待
        implicit_wait = self._config.get("implicit_wait", 10)
        self._driver.implicitly_wait(implicit_wait)

        # 设置页面加载超时
        page_load_timeout = self._config.get("page_load_timeout", 30)
        self._driver.set_page_load_timeout(page_load_timeout)

        # 设置脚本执行超时
        script_timeout = self._config.get("script_timeout", 30)
        self._driver.set_script_timeout(script_timeout)

        # 最大化窗口（如果不是headless模式）
        if not self._config.get("headless", False):
            try:
                self._driver.maximize_window()
            except:
                logger.warning("最大化窗口失败，可能处于headless模式或远程执行")

    @property
    def get_driver(self) -> Optional[webdriver.Remote]:
        return self._driver

    def quit(self):
        """关闭浏览器驱动"""
        if self._driver:
            try:
                self._driver.quit()
                logger.info("浏览器驱动已关闭")
            except Exception as e:
                logger.error(f"关闭浏览器驱动时出错: {e}")
            finally:
                self._driver = None

    def __enter__(self):
        self.create_driver()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.quit()
