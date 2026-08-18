import functions
from assertpy import assert_that


class TestFactorialFeature:

    def test_factorial_6(self):

        actual_result = functions.factorial(6)
        assert_that(actual_result).is_close_to(715, 5)


    def test_factorial_negative(self):

        has_expected_error = False

        try:
            functions.factorial(5)
        except TypeError:
            has_expected_error = True
        finally:
            assert_that(has_expected_error, 'Expected found TypeError but it doesnt').is_true()
