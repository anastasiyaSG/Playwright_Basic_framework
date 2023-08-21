import time

from playwright.sync_api import Playwright, sync_playwright, expect
import pytest

from pom.home_page_elements import HomePage
from pom.login_page_elements import LoginPage


@pytest.mark.parametrize("username", ["pesho", "gosho", "kiro", ""])
@pytest.mark.parametrize("password", ["123", "ahah", "shhs", ""])
def test_invalid_credentials(login_set_up, username, password) -> None:
    page = login_set_up

    expect(page.locator("#error")).to_be_visible()

@pytest.mark.parametrize("username", ["student"])
@pytest.mark.parametrize("password", ["Password123"])
def test_valid_credentials(login_set_up, username, password) -> None:
    page = login_set_up
    page = HomePage(page)

    expect(page.login_successfully).to_be_visible()


@pytest.mark.parametrize("username", ["student"])
@pytest.mark.parametrize("password", ["Password123"])
def test_logout_successful(login_set_up, username, password) -> None:
    page = login_set_up
    time.sleep(2)
    page = HomePage(page)

    page.logout.click()

    expect(page.login_heading).to_be_visible()