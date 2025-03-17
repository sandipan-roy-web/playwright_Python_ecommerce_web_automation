from playwright.sync_api import Page, expect
import time


def intercepted_request(route):
    route.continue_("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=67b9cc1ec019fb1ad606e6f0")


def test_network(page: Page):
    # we went to the url -> we mocked the api call to return no orders available-> asserted the same using route()
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercepted_request)
    page.get_by_placeholder("email@example.com").fill('sandi123@gmail.com')
    page.get_by_placeholder('enter your passsword').fill('S@ndipan1')
    page.get_by_role('button', name='login').click()
    page.get_by_role("button", name='ORDERS').click()
    page.get_by_role("button",name="View").first.click()


