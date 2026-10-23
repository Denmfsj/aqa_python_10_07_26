import time

from playwright.sync_api import sync_playwright, expect


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com")

    print(page.url)

    broken_images_loc = page.locator('//a[text()="Broken Images"]')  # кажемо адресу
    checkbox_loc = page.locator('//a[text()="Checkboxes"]')  # кажемо адресу

    checkbox_loc.click()  # --> https://the-internet.herokuapp.com/checkboxes

    #
    checkboxes_label = page.locator('//h3[text()="Checkboxes"]')
    expect(checkboxes_label).to_contain_text('Checkboxes')

    checkbox_1 = page.locator('//input').nth(0)
    checkbox_2 = page.locator('//input').nth(1)

    expect(checkbox_2).not_to_be_checked()

    print(checkbox_1.is_checked())
    page.wait_for_timeout(1*1000)
    checkbox_1.click()
    page.wait_for_timeout(1*1000)
    print(checkbox_1.is_checked())






    # page.goto("https://the-internet.herokuapp.com")
    #
    # page.locator('//a[text()="Dropdown"]').click()
    #
    # page.wait_for_timeout(1*1000)
    # page.eval_on_selector(
    #     "//select[@id='dropdown']",
    #     "el => el.options[el.selectedIndex].text",
    #
    # )





   #  some_text = page.get_by_role('link').nth(0) # ==> //a(1)

    # page.get_by_role("button", name="Sign up") # ==> //button[@name='Sign up']

    # page.get_by_test_id('asd')  # //*[test-id={asd}]

    # broken_images_loc.click()  # шукаємо і робимо дію
    # print(page.url)
    #
    # # print(some_text.all_inner_texts())
    #
    # page.wait_for_timeout(3*1000)
    # page.goto("https://the-internet.herokuhttps://the-internet.herokuapp.com/app.com")
    # page.wait_for_timeout(3*1000)
    #
    # # two_factor_page_loc = page.get_by_text('Two-Factor Login1')
    # # first_input_loc = page.locator('//input').nth(0)
    #
    # #page.mouse.wheel(0, 1000)
    #
    # #page.wait_for_timeout(3*1000)
    # #page.mouse.wheel(0, -300)
    #
    # page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    # two_factor_page_loc.click(timeout=4 * 1000)
    #
    # first_input_loc.fill('den')
    # page.wait_for_timeout(1 * 1000)
    #
    # first_input_loc.fill('Alice')
    # page.wait_for_timeout(0.5 * 1000)
    #
    # first_input_loc.type(' New name')
    #
    # page.wait_for_timeout(0.5 * 1000)
    # first_input_loc.press('Backspace')
    # page.wait_for_timeout(0.5 * 1000)
    # first_input_loc.press('Backspace')



    time.sleep(5)

