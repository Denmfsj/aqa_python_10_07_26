from assertpy import assert_that, soft_assertions

class AssertProductPages:


    def assert_main_page_name_price_is_equal_to_details_page(
            self, main_page_product_name, main_page_product_price, product_detail_page_name, product_detail_page_price):
        with soft_assertions():

            assert_that(main_page_product_name, f'Main page name is {main_page_product_name}'
                        ).is_equal_to(product_detail_page_name)
            assert_that(main_page_product_price, f'Main page price is {main_page_product_price}'
                        ).is_equal_to(product_detail_page_price)