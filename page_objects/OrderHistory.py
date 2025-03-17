from .OrderDetails import OrderDetailsPage


class OrderHistoryPage:
    def __init__(self,page):
        self.page = page

    def view_order_details(self,order_id):
        self.page.locator("tr").filter(has_text=order_id).get_by_role("button", name='View').click()
        order_details =  OrderDetailsPage(self.page)
        return order_details
