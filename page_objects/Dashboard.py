from playwright.sync_api import expect

from .OrderHistory import OrderHistoryPage
from .ProductDetails import  ProductDetails


class Dashboard:
    def __init__(self,page):
        self.page = page

    def navigate_orders_list(self):
        self.page.get_by_role("button", name='ORDERS').click()
        order_history = OrderHistoryPage(self.page)
        return order_history

    def fashion_checkbox(self):
        self.page.locator("//section[@id='sidebar']//div[3]//div[2]//input[1]").check()

    def check_fashion_prods(self):
        expect(self.page.get_by_text("ZARA COAT 3")).to_have_text("ZARA COAT 3")
        expect(self.page.get_by_text("ADIDAS ORIGINAL")).to_have_text('ADIDAS ORIGINAL')

    def enter_data_in_search_bar_and_validate_search_result(self):
        self.page.locator("//div[@class='py-2 border-bottom ml-3']//input[@placeholder='search']").fill('ZARA')
        self.page.keyboard.press("Enter")
        expect(self.page.get_by_text("ZARA COAT 3")).to_have_text("ZARA COAT 3")
        expect(self.page.get_by_text("Showing 1 results   | ")).to_have_text("Showing 1 results   | ")
        self.page.get_by_role('button',name='View').click()
        product_details = ProductDetails(self.page)
        return product_details


