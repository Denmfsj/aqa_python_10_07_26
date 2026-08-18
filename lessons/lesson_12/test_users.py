from assertpy import soft_assertions, assert_that


def get_users(return_empty_list=False):

    if return_empty_list:
        return []

    return [
        {'id': 1, 'name': 'Den', 'age': 20, 'job': [{'id': 1, 'title': 'QA'}]},
        {'id': 2, 'name': 'Alex', 'age': 30},
        {'id': 3, 'name': 'Igor', 'age': 40, 'job': None},
        {'id': 4, 'name': 'Ivan', 'age': 50, 'job': [{'id': 2, 'title': 'CEO'}]},
        {'id': 5, 'name': 'Mor', 'age': 60, 'job': [{'id': 1, 'title': 'QA'}]},
        {'id': 6, 'name': 'Viktor', 'age': 70, 'job': [{'id': 3, 'title': 'Retired'}]},
        {'id': 7, 'name': 'Maria', 'age': 20, 'job': [{'id': 1, 'title': 'DevOps'}]},
        {'id': 8, 'name': 'Anna', 'age': 20, 'job': []},
        {'id': 9, 'name': 'Olha', 'job': [{'id': 1, 'title': 'DevOps'}]},
    ]


def assert_user_job_is_not_empty_list(user: dict):

    user_id = user.get("id")
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

    def test_users_has_job(self):
        """
        each user must have job and it nust be not empty list
        """

        users = get_users()

        # помилка яка можу заблокувати порходження тесту. Якщо впаде - тест не продовжиться
        assert_that(len(users), 'We have to work with NOT empty list').is_greater_than(0)

        # дозволяє НЕ падати тесту при першому ASSERT.
        # Але повалить тест в кінці якщо були assertationError помилки
        with soft_assertions():

            # одне обов'язкове падіння в soft_assertions
            assert_that(0,'Test check INSIDE soft assertation' ).is_not_equal_to(0)
            for user in users:
                assert_user_job_is_not_empty_list(user)




