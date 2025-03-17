from playwright.sync_api import Page, expect,Playwright

from utils.rest_apis import RestApis

mocked_response ={"data":[],"message":"No Orders"}
def intercepted_response(route):
    route.fulfill(
        json= mocked_response
    )

def test_network(page:Page):
    # we went to the url -> we mocked the api call to return no orders available-> asserted the same using route()
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*",intercepted_response)
    page.get_by_placeholder("email@example.com").fill('sandi123@gmail.com')
    page.get_by_placeholder('enter your passsword').fill('S@ndipan1')
    page.get_by_role('button', name='login').click()
    page.get_by_role("button", name='ORDERS').click()
    expect(page.locator(".mt-4")).to_have_text("You have No Orders to show at this time. Please Visit Back Us")


def test_add_token_local_storage(playwright:Playwright):
    rest_api = RestApis()
    token = rest_api.get_token(playwright)
    browser = playwright.chromium.launch(headless=False)
    context =  browser.new_context()
    page = context.new_page()
    #script to inject token in local storage
    page.add_init_script(f"""localStorage.setItem('token','{token}')""")
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name='ORDERS').click()
    expect(page.get_by_text("Your Orders")).to_be_visible()




