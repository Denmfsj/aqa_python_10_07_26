from core.ui.sause_demo.locators.product_page import ProductPageLocators
from core.ui.sause_demo.pages.base_page import BasePage
from utils.settings import d_settings

from playwright.sync_api import sync_playwright, expect


class ProductPage(BasePage):

    header_search_loc = '//div[@class="container upper"]//a[text()="Search"]'
    # side_menu_loc = '#main-menu'
    # product_cards_block_loc = '#page-content section'

    def __init__(self, page):
        super().__init__(page, base_url=d_settings.SAUSE_DEMO_BASE_URL)
        self.full_url = ''
        self.locators = ProductPageLocators

        # self.header_search_loc = self.page.locator(
        #     '//div[@class="container upper"]//a[text()="Search"]'
        # )


    def is_page_loaded(self):

        # header_is_vis = self.page.locator(self.locators.header_search_loc).is_visible(timeout=3*1000)
        # side_menu_is_vis = self.page.locator(self.locators.side_menu_loc).is_visible(timeout=3*1000)
        # product_cards_is_vis = self.page.locator(self.locators.product_cards_block_loc
        #                                          ).is_visible(timeout=3*1000)
        #
        # return all([header_is_vis, side_menu_is_vis, product_cards_is_vis])

        return all([self.header_el_status(), self.side_menu_is_vis_status(),
                    self.product_cards_block_status()])


    def header_el_status(self):
        return self.page.locator(self.locators.header_search_loc).is_visible(timeout=3*1000)

    def side_menu_is_vis_status(self):
        return self.page.locator(self.locators.side_menu_loc).is_visible(timeout=3*1000)

    def expect_side_menu_is_visible(self):  # with assertation error

        expect(self.page.locator(self.locators.header_search_loc)).to_be_visible(timeout=15*1000)

    def product_cards_block_status(self):
        return self.page.locator(self.locators.product_cards_block_loc).is_visible(timeout=3*1000)
