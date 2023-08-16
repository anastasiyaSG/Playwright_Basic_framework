import pytest
from pom.login_page_elements import LoginPage
from playwright.sync_api import Playwright


@pytest.fixture()
def set_up(page):
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.set_default_timeout(3000)

    yield page


@pytest.fixture()
def login_set_up(set_up, password, username):
    page = set_up

    login_page = LoginPage(page)
    login_page.username.fill(username)
    login_page.password.fill(password)
    login_page.submit.click()

    yield page


@pytest.fixture(scope='session')
def context_creation(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.set_default_timeout(3000)

    login_page = LoginPage(page)
    login_page.username.fill("student")
    login_page.password.fill("Password123")
    login_page.submit.click()

    yield context

@pytest.fixture()
def login_session(context_creation):
    context = context_creation
    page = context.new_page()
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.set_default_timeout(3000)

    yield page

