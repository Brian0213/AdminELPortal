# import os
# import subprocess
# import webbrowser
#
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.chrome.options import Options
#
#
# @pytest.fixture()
# def setup(browser):
#     options = Options()
#     options.add_argument("--log-level=3")
#     options.add_argument("start-maximized")
#     options.add_argument("--disable-extensions")
#     options.add_argument("--disable-infobars")
#     options.add_argument("--disable-notifications")
#     options.add_argument("--disable-popup-blocking")
#     options.add_argument("--disable-gpu")
#     options.add_argument("--disable-dev-shm-usage")
#     options.add_experimental_option('excludeSwitches', ['enable-logging'])
#     # Uncomment this line for CI/headless runs:
#     # options.add_argument("--headless=new")
#
#     global elportal
#     if browser == 'chrome':
#         elportal = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
#     elif browser == 'firefox':
#         elportal = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
#     else:
#         raise ValueError("Unsupported browser! Use chrome or firefox.")
#
#     elportal.implicitly_wait(5)
#     yield elportal
#     elportal.quit()
#
#
# def pytest_addoption(parser):
#     """Allows passing browser type from CLI."""
#     parser.addoption("--browser", action="store", default="chrome",
#                      help="Browser to run tests with: chrome or firefox")
#
#
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")
#
#
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     """Capture screenshot automatically on test failure."""
#     outcome = yield
#     rep = outcome.get_result()
#     if rep.failed:
#         driver = item.funcargs.get("setup", None)
#         if driver:
#             os.makedirs("screenshots", exist_ok=True)
#             filename = f"screenshots/{item.name}.png"
#             driver.save_screenshot(filename)


import os
import subprocess
import webbrowser

from selenium import webdriver
import pytest
from pathlib import Path
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options


options = Options()

@pytest.fixture()
def setup(browser):
    options = webdriver.ChromeOptions()
    options.add_argument("--log-level=3")
    options.add_argument("start-maximized")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    #options.add_argument("headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    global elportal
    if browser == 'chrome':
        elportal= webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    elif browser == 'firefox':
        elportal = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    return elportal


def pytest_addoption(parser):    # This will get the value from CLI/hooks
    parser.addoption("--browser",
                     action="store",
                     default="chrome",
                     help="Browser to run tests with: chrome or firefox")

@pytest.fixture()
def browser(request):    # This will return the Browser value to the setup method.
    return request.config.getoption("--browser")



def pytest_sessionfinish(session, exitstatus):
    """ Automatically open HTML report after test run """
    html_report_path = os.path.abspath("Reports/autorep.html")
    if os.path.exists(html_report_path):
        print(f"\nOpening test report: {html_report_path}")
        try:
            webbrowser.open(f"file://{html_report_path}")
        except Exception as e:
            print(f"Failed to open report automatically: {e}")
    else:
        print("Test report not found: Reports/autorep.html")


def pytest_sessionfinish(session, exitstatus):
    """Auto-launch Allure report in browser after test run (pass or fail)"""
    allure_results_dir = os.path.abspath("AllureReport")

    if os.path.exists(allure_results_dir):
        try:
            print(f"\nLaunching Allure report from: {allure_results_dir}")
            subprocess.Popen(["allure", "serve", allure_results_dir], shell=True)
        except Exception as e:
            print(f"Failed to serve Allure report: {e}")
    else:
        print("Allure results directory not found. Did you run with --alluredir=AllureReport?")




# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests with")


