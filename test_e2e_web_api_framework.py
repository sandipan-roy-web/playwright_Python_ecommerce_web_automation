import json
import pytest
from playwright.sync_api import Playwright, Page, expect
from page_objects.LoginPage import LoginPage
from utils.rest_apis import RestApis

with open("data/credentials.json") as f:
    test_data = json.load(f)    #loads json as dictionary
    user_data = test_data['user_credentials']
@pytest.mark.parametrize('user_cred',user_data)
def test_login_via_api(playwright: Playwright,page:Page,user_cred):  #the user_cred here is a fixture in conftest file
    #login -> create order-> get order _id
    email = user_cred['user_email']
    passwd = user_cred['user_pass']
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    login_page =  LoginPage(page)
    login_page.navigate()
    dashboard = login_page.login(email,passwd)
    restapi =RestApis()
    order_id = restapi.create_order(playwright,user_cred)
    # # -> check orders-> match with the value available on the order list->click view
    order_history = dashboard.navigate_orders_list()
    order_details = order_history.view_order_details(order_id)
    order_details.verify_order_success_message()

@pytest.mark.parametrize('user_cred',user_data)
#login -> dashboard,click on the fashion checkbox ->validate products shown
def test_fashion_checkbox_click(playwright:Playwright,user_cred):
    email = user_cred['user_email']
    passwd =  user_cred['user_pass']
    browser = playwright.chromium.launch(headless=False)
    context =  browser.new_context()
    page = context.new_page()
    login = LoginPage(page)
    login.navigate()
    dash = login.login(email, passwd)
    dash.fashion_checkbox()
    dash.check_fashion_prods()


@pytest.mark.parametrize('user_cred',user_data)
#login->search for ZARA->Press Enter->Validate search result->click on View of that product->Check continue shopping button
def test_search_bar_on_dashboard(playwright:Playwright,user_cred):
    browser = playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page = context.new_page()
    email = user_cred['user_email']
    passwd = user_cred['user_pass']
    login=LoginPage(page)
    login.navigate()
    dashboard = login.login(email, passwd)
    product_details = dashboard.enter_data_in_search_bar_and_validate_search_result()
    product_details.validate_continue_shopping_button_is_visible()









