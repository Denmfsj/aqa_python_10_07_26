import time

import functions
import assertpy
import pytest
import logging
logging.basicConfig(level=logging.DEBUG, force=True)



class TestTriangleArea:

    # fixture
    user_id = 10



    @pytest.fixture
    def my_own_pre_post_condition(self):
        # до слова yeild - precondition
        time.sleep(1)
        logging.info(f'Creating user with id = {self.user_id}')

        yield  # після - postcondition
        logging.info(f'Deleting user with id = {self.user_id}')


    def test_triangle_area_smoke(self, my_own_pre_post_condition):


        actual_result = functions.triangle_area(1,3,3)
        expected_result = 1.479019945774904

        assertpy.assert_that(actual_result,
                             f'Expected: {expected_result}').is_equal_to(expected_result)

    def test_triangle_area_regression(self):


        actual_result = functions.triangle_area(4,3,5 )
        expected_result = 6.0

        assertpy.assert_that(actual_result,
                             f'Expected: {expected_result}').is_equal_to(expected_result)



