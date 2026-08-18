import functions


class TestFactorialFeature:

    def test_factorial_1(self):

        actual_result = functions.factorial(1)
        expected_result = 1

        assert actual_result == expected_result, (f"Factorial from 1 must "
                                                  f"be {expected_result} but it is {actual_result}")


    def test_factorial_5(self):

        actual_result = functions.factorial(5) # 120
        expected_result = 121

        assert actual_result == expected_result, (f"Factorial from 5 must "
                                                  f"be {expected_result} but it is {actual_result}")


    def test_factorial_2(self):

        actual_result = functions.factorial('2') # 2
        expected_result = 2

        assert actual_result == expected_result, (f"Factorial from 2 must "
                                                  f"be {expected_result} but it is {actual_result}")

