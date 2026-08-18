import json
from pathlib import Path

import pytest
from assertpy import soft_assertions, assert_that


def get_users():  # повернення данних з файла як масив

    file_path = Path(__file__).parent / 'users.json'

    with open(file_path) as f:
        return json.loads(f.read())


def assert_user_job_is_not_empty_list(user: dict):

    user_id = user["id"]
    actual_user_data = user.get('job')
    actual_type_of_job = type(actual_user_data)
    star_of_error_message = f'User {user_id} must have'

    # assert_that(what_we_are_checking, error_message).what_we_check()

    assert_that(actual_type_of_job,
                f'{star_of_error_message} job list'
                ).is_equal_to(list)

    if type(actual_user_data) is list:
        assert_that(len(actual_user_data),
                    f'{star_of_error_message} NOT EMPTY job list'
                    ).is_greater_than(0)


class TestUsers:

    @pytest.mark.parametrize('user',
                             get_users()  # список словників(юзерів)
                             )
    def test_users_has_job(self, user):
        """
        each user must have job and it nust be not empty list
        """

        with soft_assertions():
            assert_user_job_is_not_empty_list(user)




