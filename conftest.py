import pytest
from playwright.sync_api import sync_playwright

# Base URL for web
@pytest.fixture(scope="session")
def base_url():
    return "https://stg-resident-admin.lumi.biz"

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chromium", help="chromium or firefox")

# Browser name
@pytest.fixture(scope="session")
def browser_name(pytestconfig):
    return pytestconfig.getoption("browser_name")

# Playwright
@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as playwright:
        yield playwright

# Browser
@pytest.fixture(scope="session")
def browser(playwright, browser_name):
    if browser_name == "chromium":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    yield browser
    browser.close()

# Context
@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

# Page
@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()

# New context for testing remember login
@pytest.fixture(scope="function")
def new_context(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture(scope="function")
def refresh_page(page):
    page.reload()


