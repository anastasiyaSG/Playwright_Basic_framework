import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

from pom.home_page_elements import HomePage


@pytest.mark.skip(reason="personal")
def test_logo(login_session) -> None:
    page = login_session
    home_page = HomePage(page)

    expect(home_page.logo).to_be_visible()


def test_logo_successful(login_session) -> None:
    page = login_session
    home_page = HomePage(page)

    expect(home_page.logo).to_be_visible()
