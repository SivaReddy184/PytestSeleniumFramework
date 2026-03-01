import pytest
import allure
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def pytest_addoption(parser):
    parser.addoption("--browser", action='store', default='chrome', help='Type of browser: chrome,edge,ff')
    parser.addoption("--headless", action='store', default='false', help='true or false')


def pytest_sessionfinish(session, exitstatus):
    """
    This hook runs after the entire test suite finishes.
    It creates the environment.properties file inside the allure-results folder.
    """
    allure_results_path = os.path.join(session.config.rootdir, 'reports', 'allure-results')

    # Ensure the directory exists
    if not os.path.exists(allure_results_path):
        os.makedirs(allure_results_path)

    browser_name = session.config.getoption("--browser")
    # Define your environment details
    env_details = (
        f"Project=E-Commerce-Client-App\n"
        "Environment=QA\n"
        f"Browser={browser_name}\n"
        "Tester=Siva\n"
        "OS=Windows 11"
    )

    with open(os.path.join(allure_results_path, 'environment.properties'), 'w') as f:
        f.write(env_details)



@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call' and report.failed:
        # Get the driver instance from the test class
        driver = getattr(item.cls, 'driver', None)
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Failure_Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

@pytest.fixture(scope='class')
def browser_setup(request):
    browser = request.config.getoption("--browser").lower()
    headless = request.config.getoption("--headless").lower()

    if browser == 'chrome':
        ops = ChromeOptions()
        if headless == 'true':
            ops.add_argument("--headless")
            ops.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=ops)

    elif browser == 'firefox':
        ops = FirefoxOptions()
        if headless == 'true':
            ops.add_argument("--headless")
            ops.add_argument("--window-size=1920,1080")
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()),options=ops)

    elif browser == 'edge':
        ops = EdgeOptions()
        if headless == 'true':
            ops.add_argument("--headless")
            ops.add_argument("--window-size=1920,1080")
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()),options=ops)

    else:
        raise pytest.UsageError('--browser must be chrome, firefox or edge')

    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()
