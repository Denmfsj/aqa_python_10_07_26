import time


def test_if_number_is_odd(number):

    # if number % 2 == 0:
    #     raise AssertionError('The number is NOT odd')  # помилка = bug

    # assert not (number % 2 == 0), "The number is NOT odd"  # -->  raise AssertionError(The number is NOT odd)
    assert number % 2 != 0, "The number is NOT odd"  # -->  raise AssertionError(The number is NOT odd)


# test_if_number_is_odd(8)


def wait_n_sec_server_answer(message_id: str, number_of_sec_to_wait: int = 30):

    start = time.time()

    while time.time() - start < number_of_sec_to_wait:  # чекати number_of_sec_to_wait секунд

        resp = request.send(message_id)

        if resp.status_code == 200:  # прийшла правильна відповідь
            return resp.text
        else:
            time.sleep(1)

    raise NameError('Server return no answer for message {}'.format(message_id))


