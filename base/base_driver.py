from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from utils.custom_logger import LogGen


class BasePage:
    logger = LogGen.loggen()

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def do_click(self, locator):
        self.logger.info(f"Clicking on the element with locator {locator}")
        try:
            self.wait.until(EC.visibility_of_element_located(locator)).click()
        except Exception as e:
            self.logger.info(f"Failed to click on locator {locator}. Error {e}")
            raise

    def do_send_keys(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        self.logger.info(f"Entering text with the locator {locator}")
        element.send_keys(text)

    def get_element_text(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.logger.info(f"Getting the locator {locator} text")
        return element.text

    # property decorator so that we can call it as variable rather than a function
    @property
    def get_current_url(self):
        return self.driver.current_url

