from playwright.sync_api import Playwright, sync_playwright, expect
import pytest

from pom.login_page_elements import LoginPage


@pytest.mark.parametrize("username", ["pesho", "gosho", "kiro"])
@pytest.mark.parametrize("password", ["123", "ahah", "shhs"])
def test_invalid_credentials(login_set_up, username, password) -> None:
    page = login_set_up

    expect(page.locator("#error")).to_be_visible()


