import time

from playwright.sync_api import Page, expect


def test_playwright_basic(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page= context.new_page()
    page.goto("https://www.dezerv.in/portfolio-management-services/#problem")


def test_playwright_basics2(page:Page):
    page.goto("https://www.dezerv.in/portfolio-management-services/#problem")



def test_login_page_rahul_shetty_academy(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.locator("#signInBtn").click()
   # page.get_by_role("button",name="Sign In").click()  # this will click on the Sign in button using the button
    #page.get_by_role("checkbox",name="terms").check()  #this will check the checkbox in the login box
    time.sleep(5)

def test_login_page_with_invalid_cred(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learnin1")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.locator("#signInBtn").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()

def test_adding_products_to_checkout(page:Page):
    #Added iphonex and samsungproduct to the cart and verified the count in checkout
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.locator("#terms").check()
    page.locator("#signInBtn").click()
    iphone_x_product = page.locator("app-card").filter(has_text="iphone X") #this will filter based on text and fine iphoneX
    iphone_x_product.get_by_role("button").click()
    samsung_product = page.locator("app-card").filter(has_text="Samsung Note 8")
    samsung_product.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media")).to_have_count(2)
    time.sleep(5)

def test_child_window(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as new_page_info:
        #handles child window ,moment the child page open it stores in new_page_info
        page.get_by_role("link",name="Free Access to InterviewQues/ResumeAssistance/Material").click()
        child_window = new_page_info.value
        text = child_window.locator(".im-para.red ").text_content()
        words = text.split('at')
        email = words[1].split(' ')[1]
        assert email == 'mentor@rahulshettyacademy.com'


def  test_handle_alerts(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.on('dialog',lambda dialog:dialog.accept())
    # this is going to look for alert (dialog) and the lambda dialog:dialog.accept is a function
    time.sleep(5)
    page.locator('#alertbtn').click()






