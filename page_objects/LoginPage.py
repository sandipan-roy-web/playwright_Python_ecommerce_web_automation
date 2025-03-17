from .Dashboard import Dashboard


class LoginPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client")

    def login(self, email, passwd):
        self.page.get_by_placeholder("email@example.com").fill(email)
        self.page.get_by_placeholder('enter your passsword').fill(passwd)
        self.page.get_by_role('button', name='login').click()
        dashboard = Dashboard(self.page)
        return dashboard


