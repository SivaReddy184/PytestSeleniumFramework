from selenium.webdriver.common.by import By
from base.base_driver import BasePage


class Login(BasePage):
    EMAIL_FIELD = (By.ID, "userEmail")
    PASSWORD_FIELD = (By.ID, "userPassword")
    LOGIN_BTN = (By.NAME, "login")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".toast-container")

    def __init__(self, driver):
        super().__init__(driver)

    def login_to_application(self, email, password):
        self.do_send_keys(self.EMAIL_FIELD, email)
        self.do_send_keys(self.PASSWORD_FIELD, password)
        try:
            self.driver.execute_script("argument[0].scrollIntoView(true);", self.driver.find_element(*self.LOGIN_BTN))
            self.do_click(self.LOGIN_BTN)

        except Exception as e:
            self.driver.execute_script("arguments[0].click();", self.driver.find_element(*self.LOGIN_BTN))

    def get_error_text(self):
        return self.get_element_text(self.ERROR_MESSAGE)

    def get_login_page_url(self):
        return self.get_current_url

