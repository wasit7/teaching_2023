from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.google.com/search?q=%E0%B9%81%E0%B8%A1%E0%B8%A7&tbm=shop")
    print(page.title())
    # browser.close()
    # print(page.content())
    with open("shop.html", "w") as file:
        file.write(page.content())