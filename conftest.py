from email.policy import default
from optparse import Option
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOption
from selenium.webdriver.firefox.options import Options as FFOptions


def pytest_addoption(parser):
    parser.addoption("--browser", default="ch")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--url", default="localhost")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    base_url = request.config.getoption("--url")

    driver = None

    if browser_name == "ch":
        options = ChromeOption()
        if headless:
            options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)
    elif browser_name == "ff":
        options = FFOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    elif browser_name == "edge":
        driver = webdriver.Edge()
    elif browser_name == "ya":
        options = ChromeOption()
        if headless:
            options.add_argument("--headless=new")
        options.binary_location = "/usr/bin/yandex-browser"
        driver = webdriver.Chrome(
            service=Service(
                executable_path="/home/mikhail/Downloads/drivers/yandexdriver",
            ),
            options=options,
        )
    else:
        raise ValueError(f"Driver for {browser_name} not supported")

    driver.base_url = base_url

    yield driver

    driver.quit()
