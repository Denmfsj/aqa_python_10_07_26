from core.ui.sause_demo.locators.product_page import ProductPageLocators
from core.ui.sause_demo.pages.base_page import BasePage
from utils.settings import d_settings


class ProductDetailsPage(BasePage):


    def __init__(self, page, product_id):
        super().__init__(page, base_url=d_settings.SAUSE_DEMO_BASE_URL)
        self.full_url = f'collections/frontpage/products/{product_id}'
        self.locators = ProductPageLocators

    def _product_form(self):
        locator = self.page.locator('#product-form')
        locator.is_visible(timeout=3*1000)
        return locator

    def get_product_name(self) -> str:
        return self._product_form().locator('//h1').text_content().strip()

    def get_product_price(self) -> str:
        return self._product_form().locator('//h2/span').text_content().strip()
