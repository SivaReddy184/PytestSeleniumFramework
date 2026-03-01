import os.path
import pytest

from pages.login_page import Login
from utils.custom_logger import LogGen
from utils.excel_utils import ExcelUtils


@pytest.mark.usefixtures("browser_setup")
class Test_002_DDT_Login:
    path = os.path.abspath(r"C:\Users\ASUS\Desktop\Projects\PythonSeleniumFramework\testdata\data.xlsx")
    logger = LogGen.loggen()
    @pytest.mark.parametrize("usr, pwd, exp", ExcelUtils.get_data_from_excel(path, "data"))
    def test_login_ddt(self, usr, pwd, exp):
        self.logger.info(f"******* Testing Login for User: {usr} *******")
        login_page = Login(self.driver)
        self.driver.get("https://rahulshettyacademy.com/client")
        login_page.login_to_application(usr, pwd)
        actual_result = "dash" in self.driver.current_url

        if exp == "Pass":
            if actual_result:
                self.logger.info("Login successful as expected.")
                assert True
            else:
                self.logger.error("Login failed but expected Pass.")
                assert False

        elif exp == "Fail":
            if actual_result:
                self.logger.error("Login passed but expected Fail.")
                assert False
            else:
                self.logger.info("Login failed as expected.")
                assert True
