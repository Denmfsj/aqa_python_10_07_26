import time

from playwright.sync_api import sync_playwright, expect


h2_main_text_css_loc = "div#content h2"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)


    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com")


    # for loc in ('#table-ann', '#table-q'):
    #     table_el = page.locator(loc)
    #
    #     table_el.locator('//div[@data-id="net_value"]')


    h2_main_text_locator = page.locator(h2_main_text_css_loc)  # css
    table_loc = page.locator("//ul")

    h2_table_text_locator = table_loc.locator(h2_main_text_css_loc)  # css

    expect(h2_main_text_locator).to_be_visible(timeout=3*1000)  # 3 sec
    expect(table_loc).to_be_visible(timeout=3*1000)
    # expect(h2_table_text_locator).to_be_visible(timeout=3*1000)

    # page.goto("https://the-internet.herokuapp.com/dropdown")
    #
    # dropdown_el = page.locator("select")
    #
    # dropdown_el.select_option('1')
    # time.sleep(1)
    # dropdown_el.select_option(label='Option 2')
    # time.sleep(1)

    page.goto("https://the-internet.herokuapp.com/windows")


    with page.context.expect_page() as new_page_info:
        page.locator("//a[@target='_blank']").nth(0).click(timeout=3*1000)

    newpage = new_page_info.value

    print(newpage.locator('//h3').text_content(timeout=3*1000))

    time.sleep(1)
    newpage.close()

    expect().is_visible()

    assert page.locator("//a[@target='_blank']").nth(0).is_visible(), "Cant find link to new window"
    time.sleep(1)



