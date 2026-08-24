import functions
import assertpy


def test_converts_24_hours():

    base_value = '5:45 PM'
    expected_result = '17:45'

    actual_result = functions.convert_to_24_hour(base_value)

    assertpy.assert_that(actual_result,
                         f'Expected: {expected_result}').is_equal_to(expected_result)


def test_converts_24_hours_negative():

    try:
        functions.convert_to_24_hour([])
    except TypeError:
        pass
    else:
        assertpy.fail('Expected TypeError but it wasnt')
        # assert False, 'Expected TypeError but it wasnt'


