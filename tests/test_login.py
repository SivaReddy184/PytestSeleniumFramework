import os

import allure
import dotenv
import pytest
from dotenv import load_dotenv

from pages.login_page import Login
from utils.custom_logger import LogGen
load_dotenv()

@allure.epic("Ecommerce web application")
@allure.feature("Login Module")
@pytest.mark.usefixtures("browser_setup")
class TestLogin:

    logger = LogGen.loggen()
    @allure.story("Valid login test")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.flaky(reruns=2)
    def test_valid_login(self):
        self.logger.info("*******Starting Test login 001********")

        self.logger.info("Step 1: Navigating to login page")
        login_page = Login(self.driver)


        with allure.step("Navigate to application"):
            self.driver.get("https://rahulshettyacademy.com/client")

        self.logger.info(f"Step 2: Entering email {login_page.EMAIL_FIELD}")
        with allure.step("Enter login credentials"):
            login_page.login_to_application(os.getenv("personal_email"), os.getenv("personal_password"))

        self.logger.info("Step 3: Verifying page title")
        with allure.step("Verify page title"):
            self.logger.info("Verifying page title")
            act_title = self.driver.title

            if act_title == "Let's Shop":
                self.logger.info("********Test Login 001 Passed")
                assert True

            else:
                self.logger.error("**** Login Test Failed: Title Mismatch ****")
                self.driver.save_screenshot(".\\Reports\\login_fail.png")
                self.logger.info("****Test Login 001 Failed****")
                assert False


    def test_invalid_login(self):
        self.logger.info('***Starting Test Invalid Login TC 002***')
        login_page = Login(self.driver)
        self.driver.get("https://rahulshettyacademy.com/client")
        self.logger.info(f"Step 2: Entering email {login_page.EMAIL_FIELD}")
        login_page.login_to_application("anshika@gmail.com", "Iamking@00")

        error = login_page.get_error_text()
        self.logger.info("Verifying error text")
        assert "Incorrect email or password" in error
        self.logger.info("Test Invalid Login TC 002 Passed")

