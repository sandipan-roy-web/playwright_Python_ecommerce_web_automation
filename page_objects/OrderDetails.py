from playwright.sync_api import expect


class OrderDetailsPage:
    def __init__(self,page):
        self.page = page

    def verify_order_success_message(self):
        expect(self.page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")