import functions
import pytest
from assertpy import assert_that


class TestFactorialFeature:

    #
    @pytest.mark.parametrize(   # виклик функції parametrize
        'original_number,expected_result', # перши аргумент: імена змінних
        [
            (1,1),
            (5, 121),
            (11, 39916800)
        ])
    def test_factorial(self, original_number, expected_result):  # в дужках аргументи це імена змінних з parametrize

        actual_result = functions.factorial(original_number)

        assert actual_result == expected_result, (f"Factorial from {original_number} must "
                                                  f"be {expected_result} but it is {actual_result}")


    #
    @pytest.mark.parametrize(   # виклик функції parametrize
        'type_error,parameter', # перши аргумент: імена змінних
        [
            (TypeError,None),
            (AssertionError, 0),
        ])
    def test_factorial(self, type_error,parameter):  # в дужках аргументи це імена змінних з parametrize

        has_expected_error = False

        try:
            functions.factorial(parameter)
        except type_error:
            has_expected_error = True
        finally:
            assert_that(has_expected_error, f'Expected found {type_error} but it doesnt').is_true()
