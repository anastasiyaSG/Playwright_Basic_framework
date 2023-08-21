import time
import pytest
from pytest_playwright_visual.plugin import assert_snapshot

from pom.login_page_elements import LoginPage

def test_login_page(set_up, assert_snapshot) -> None:
    page = set_up

    assert_snapshot(page.screenshot(mask=[page.locator(".nav")]))

@pytest.mark.parametrize("username", ["student"])
@pytest.mark.parametrize("password", ["Password123"])
def test_home_page(login_set_up, username, password, assert_snapshot) -> None:
    page = login_set_up
    time.sleep(5)

    assert_snapshot(page.screenshot(mask=[page.locator(".nav")]))

@pytest.mark.parametrize("username", ["student"])
@pytest.mark.parametrize("password", ["Password123"])
def test_password_asterics(set_up, username, password, assert_snapshot) -> None:
    page = set_up

    login_page = LoginPage(page)
    login_page.username.fill(username)
    login_page.password.fill(password)

    assert_snapshot(page.screenshot())

@pytest.mark.parametrize("username", ["lorem"])
@pytest.mark.parametrize("password", ["Password123"])
def test_invalid_username(set_up, username, password, assert_snapshot) -> None:
    page = set_up

    login_page = LoginPage(page)
    login_page.username.fill(username)
    login_page.password.fill(password)
    login_page.submit.click()

    assert_snapshot(page.screenshot())

@pytest.mark.parametrize("username", ["student"])
@pytest.mark.parametrize("password", ["ipsum"])
def test_invalid_password(set_up, username, password, assert_snapshot) -> None:
    page = set_up

    login_page = LoginPage(page)
    login_page.username.fill(username)
    login_page.password.fill(password)
    login_page.submit.click()

    assert_snapshot(page.screenshot())


def test_empty_fields(set_up, assert_snapshot) -> None:
    page = set_up

    login_page = LoginPage(page)
    login_page.submit.click()

    assert_snapshot(page.screenshot())