from assertpy import soft_assertions, assert_that
from random import choice
import pytest

from playwright.sync_api import sync_playwright, expect

from utils.settings import d_settings

header_search_loc = '//div[@class="container upper"]//a[text()="Search"]'
side_menu_loc = '#main-menu'
product_cards_block_loc = '#page-content section'
product_cards_loc = '#page-content section div'


@pytest.fixture(scope='session')
def home_page():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()
        page.goto(d_settings.SAUSE_DEMO_BASE_URL)  #  hardcode - винести
        yield page


def test_smoke_product_page(home_page):

    header_is_vis = home_page.locator(header_search_loc).is_visible(timeout=3*1000)
    side_menu_is_vis = home_page.locator(side_menu_loc).is_visible(timeout=3*1000)
    product_cards_is_vis = home_page.locator(product_cards_block_loc).is_visible(timeout=3*1000)


    with soft_assertions():
        assert_that(header_is_vis, f'Cant find header, {header_search_loc}').is_true()
        assert_that(side_menu_is_vis, f'Cant find side menu, {side_menu_loc}').is_true()
        assert_that(product_cards_is_vis, f'Cant find product_cards, {product_cards_block_loc}').is_true()

def test_product_page_contains_3_cards(home_page):


    product_cards_is_vis = home_page.locator(product_cards_loc).all()

    assert_that(product_cards_is_vis, 'Expected 3 product cars on main page by default').is_length(3)


def test_product_page_comparing_product_cards_with_details_page(home_page):


    # 1 get text product_cards_loc / h3 - name
    # 2 get text product_cards_loc / h4 - price
    # 3 click по product_cards_loc / a
    # 4 locator = #product-form / h1 -  name
    # 5 locator = #product-form / h2 / span -  price


    product_cards = home_page.locator(product_cards_loc).all()

    product_el = choice(product_cards)

    main_page_product_name = product_el.locator('//h3').text_content().strip()  # обрізати /n, space, /t
    main_page_product_price = product_el.locator('//h4').text_content().strip()

    product_el.locator('//a').click()

    product_form = home_page.locator('#product-form')
    product_detail_page_name = product_form.locator('//h1').text_content().strip()
    product_detail_page_price = product_form.locator('//h2/span').text_content().strip()


    with soft_assertions():

        assert_that(main_page_product_name, f'Main page name is {main_page_product_name}'
                    ).is_equal_to(product_detail_page_name)
        assert_that(main_page_product_price, f'Main page price is {main_page_product_price}'
                    ).is_equal_to(product_detail_page_price)




