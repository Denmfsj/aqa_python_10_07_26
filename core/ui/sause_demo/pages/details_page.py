from core.ui.sause_demo.pages.base_page import BasePage
from utils.settings import d_settings


class ProductDetailPage(BasePage):

    def __init__(self, page, product_name):
        super().__init__(page, base_url=d_settings.SAUSE_DEMO_BASE_URL)
        self.full_url = f'/collections/frontpage/products/{product_name}'

