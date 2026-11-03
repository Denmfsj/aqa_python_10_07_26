import allure
import pytest
from random import choice

from logging import getLogger

from core.ui.sause_demo.assertations.assert_product_pages import AssertProductPages
from core.ui.sause_demo.pages.product_page import ProductPage
from assertpy import soft_assertions, assert_that


base_log = getLogger()

@pytest.fixture(scope='module')
def page(browser):

    page = browser.new_page()
    yield page

@pytest.fixture(scope='module')
def product_page(page):

    return ProductPage(page)

@allure.epic('Sauce Demo project')
@allure.feature('Modern style tests')
@allure.story('smoke tests')
@pytest.mark.ui
@pytest.mark.modern
def test_smoke_product_page(product_page):

    product_page.open()
    assert_that(product_page.is_page_loaded(), 'Page is not loaded').is_true()


product_asserts = AssertProductPages()

@allure.epic('Sauce Demo project')
@allure.feature('Modern style tests')
@allure.story('sanity tests')
@pytest.mark.ui
@pytest.mark.modern
def test_product_page_comparing_product_cards_with_details_page(product_page):



    print('Data in stdout to check in allure rep')

    base_log.info('Data in log files to check in allure rep')

    with allure.step('Opening page'):
        product_page.open()


    # with allure.step('Choose card'):
    product_cards = product_page.get_list_of_all_product_cards()
    product_el = choice(product_cards)

    # with allure.step('Getting data(name and price)'):
    main_page_product_name = product_page.get_product_name_from_card(product_el)
    main_page_product_price = product_page.get_product_price_from_card(product_el)


    # with allure.step('Opening details page'):
    details_page = product_page.open_product_card_details(product_el)  # open product detail page

    # with allure.step('Getting data(name and price)'):
    product_detail_page_name = details_page.get_product_name()
    product_detail_page_price = details_page.get_product_price()


    # with allure.step('Comparing data'):
    product_asserts.assert_main_page_name_price_is_equal_to_details_page(
        main_page_product_name, main_page_product_price, product_detail_page_name, product_detail_page_price
    )


    # #  product_page.page.url - урл поточної сторінки? .split('/')[-1] = noir-jacket
    # prod_id = product_page.page.url.split('/')[-1]
    #
    # details_page = ProductDetailsPage(page=product_page.page, product_id=prod_id)
