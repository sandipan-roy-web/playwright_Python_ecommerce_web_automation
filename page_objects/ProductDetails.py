from playwright.sync_api import expect


class ProductDetails:
    def __init__(self,page):
        self.page = page

    def validate_continue_shopping_button_is_visible(self):
        expect(self.page.get_by_text("Continue Shopping")).to_be_visible()