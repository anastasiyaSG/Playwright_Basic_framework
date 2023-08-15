from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.get_by_label("Username").click()
    page.get_by_label("Username").fill("juu")
    page.get_by_label("Username").press("Tab")
    page.get_by_label("Password").fill("jjj")
    page.get_by_role("button", name="Submit").click()
    page.locator("#error").click()
    page.get_by_label("Username").click()
    page.get_by_label("Username").fill("student")
    page.get_by_label("Username").press("Tab")
    page.get_by_label("Password").fill("Password123")
    page.get_by_role("button", name="Submit").click()
    page.get_by_role("heading", name="Logged In Successfully").click()
    page.get_by_role("link", name="Practice Test Automation", exact=True).click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
