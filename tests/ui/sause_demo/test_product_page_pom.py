from assertpy import soft_assertions, assert_that
from random import choice
import pytest

from playwright.sync_api import sync_playwright, expect

from core.ui.sause_demo.pages.product_page import ProductPage
from utils.settings import d_settings

@pytest.fixture(scope='session')
def page():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()
        yield page

@pytest.fixture(scope='session')
def product_page(page):

    return ProductPage(page)


def test_smoke_product_page(product_page):

    product_page.open()
    assert_that(product_page.is_page_loaded(), 'Page is not loaded').is_true()



    # if not product_page.is_page_loaded():
    #     header_status = product_page.header_el_status()
    #     side_menu_status = product_page.side_menu_is_vis_status()
    #     product_cards = product_page.product_cards_block_status()
    #
    #
    #     with soft_assertions():
    #         assert_that(header_status, f'Cant find header, '
    #                                    f'{product_page.locators.header_search_loc}').is_true()
    #         assert_that(side_menu_status, f'Cant find side menu, '
    #                                    f'{product_page.locators.side_menu_loc}').is_true()
    #         assert_that(product_cards, f'Cant find product_cards, '
    #                                    f'{product_page.locators.product_cards_block_loc}').is_true()
