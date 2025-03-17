import time

from playwright.sync_api import Playwright, Page, expect

from test_ecommerce_page import test_login_with_valid_credentials
from utils.rest_apis import RestApis


def test_login_via_api(playwright: Playwright,page:Page):
    #login -> create order-> get order _id
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill('sandi123@gmail.com')
    page.get_by_placeholder('enter your passsword').fill('S@ndipan1')
    page.get_by_role('button', name='login').click()
    restapi =RestApis()
    order_id = restapi.create_order(playwright)
    # -> check orders-> match with the value available on the order list->click view
    page.get_by_role("button",name='ORDERS').click()
    page.locator("tr").filter(has_text=order_id).get_by_role("button",name='View').click()
    #row.get_by_role("button",name='View').click()
    expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")





