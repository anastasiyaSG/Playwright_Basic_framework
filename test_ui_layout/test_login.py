from playwright.sync_api import Playwright, sync_playwright, expect
import pytest

from pom.login_page_elements import LoginPage


@pytest.mark.parametrize("username", ["pesho", "gosho", "kiro"])
@pytest.mark.parametrize("password", ["123", "ahah", "shhs"])
def test_invalid_credentials(login_set_up, username, password) -> None:
    page = login_set_up

    expect(page.locator("#error")).to_be_visible()




# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://practicetestautomation.com/practice-test-login/")
#     page.get_by_label("Username").click()
#     page.get_by_label("Username").fill("juu")
#     page.get_by_label("Username").press("Tab")
#     page.get_by_label("Password").fill("jjj")
#     page.get_by_role("button", name="Submit").click()
#     page.locator("#error").click()
#     page.get_by_label("Username").click()
#     page.get_by_label("Username").fill("student")
#     page.get_by_label("Username").press("Tab")
#     page.get_by_label("Password").fill("Password123")
#     page.get_by_role("button", name="Submit").click()
#     page.get_by_role("heading", name="Logged In Successfully").click()
#     page.get_by_role("link", name="Practice Test Automation", exact=True).click()
#
#     # ---------------------
#     context.close()
#     browser.close()
#
#
# with sync_playwright() as playwright:
#     run(playwright)
