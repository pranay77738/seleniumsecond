import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import logging
import inspect


@pytest.mark.usefixtures("setup")
class Baseclass:
    def test_logging(self):
        loggerName = inspect.stack()[1][3]
        # logger = logging.getLogger(__name__)
        logger = logging.getLogger(loggerName)
        filehandler = logging.FileHandler("logs.log")
        formatter = logging.Formatter(
            "%(asctime)s :%(levelname)s :%(name)s :%(message)s"
        )
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)

        logger.setLevel(logging.DEBUG)
        return logger

    def verifytextpresent(self, text):
        wait = WebDriverWait(self.driver, 8)
        wait.until(
            expected_conditions.presence_of_element_located((By.LINK_TEXT, text))
        )

    def selectoptionbytest(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)
