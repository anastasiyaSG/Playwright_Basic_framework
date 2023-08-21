class HomePage:
    def __init__(self, page):
        self.login_successfully = page.get_by_role("heading", name="Logged In Successfully")
        self.logo = page.get_by_role("link", name="Practice Test Automation", exact=True)
        self.logout = page.get_by_role("link", name="Log out")
        self.login_heading = page.get_by_role("heading", name="Test login")
