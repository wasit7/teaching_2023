from playwright.sync_api import Playwright, sync_playwright
import time
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://www.dataforthai.com/login')
    time.sleep(3)
    page.locator("#login-username").fill('wasit7@gmail.com')
    # time.sleep(5)
    page.locator("#login-password").fill('qwer1234')
    # time.sleep(5)
    page.locator("#btn-login").click()

    tax_ids=[
        "0102564000010",
        "0103564000011",
        "0103564000029",
        "0103564000037",
        "0103564000045",
        "0103564000053",
        "0103564000061",
        "0103564000070",
        "0103564000088",
        "0103564000096",
        "0103564000100",
        "0103564000118",
    ]
    for i in tax_ids:
        url = f'https://www.dataforthai.com/business/search/{i}'
        print(f'>>>>>>>>>>>  go to: {url}')
        page.goto(url)
        x=page.content()
        print(x)
        time.sleep(1)