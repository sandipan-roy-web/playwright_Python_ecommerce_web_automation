import time
import pytest

from playwright.sync_api import Playwright, expect


def test_data():
    return [
        #("Sandipan", "Roy", "9901347499", "sandi123@gmail.com", "S@ndipan1", "S@ndipan1"),
        ("John", "Doe", "9876543210", "joh.doe@example.com", "P@ssword123", "P@ssword123"),
    ]
def test_credentials():
    return [
        ('sandi123@gmail.com',"S@ndipan1")
    ]

@pytest.mark.parametrize('firstname,lastname,phone,email,password,confirm_password', test_data())
def test_register_new_user(playwright: Playwright, firstname, lastname, phone, email, password, confirm_password):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client")
    page.locator(".text-reset").click()
    page.locator("#firstName").fill(firstname)
    page.locator("#lastName").fill(lastname)
    page.locator("#userMobile").fill(phone)
    page.locator("#userEmail").fill(email)
    page.get_by_role("combobox").select_option('Student')
    page.locator("#userPassword").fill(password)
    page.locator("#confirmPassword").fill(confirm_password)
    page.get_by_role("checkbox").check()
    page.locator('#login').click()
    time.sleep(5)


@pytest.mark.parametrize('email ,password', test_credentials())
def test_login_with_valid_credentials(playwright: Playwright, email, password):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://rahulshettyacademy.com/client')
    page.get_by_placeholder("email@example.com").fill(email)
    page.get_by_placeholder('enter your passsword').fill(password)
    page.get_by_role('button', name='login').click()
    expect(page).to_have_url('https://rahulshettyacademy.com/client/dashboard/dash')
    time.sleep(5)

