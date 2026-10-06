import random

import pytest
from faker import Faker

from core.api.strudent_service.assertations.student_assertation import StudentAssertBase
from core.api.strudent_service.students_controller import StudentController

import logging

from tests.functional.student_service.conftest import TestStudentsBase

logger = logging.getLogger(__name__)
faker = Faker()



class TestCreateStudent(TestStudentsBase):

    student_assert = StudentAssertBase()

    st_id_for_deleting = None

    def test_create_user(self, delete_student):

        name =  faker.name()
        score = random.choice(range(60, 100))

        st = self.students_ctrl.post_student(user_data={
            "name": name,
            "score": score,
        })

        __class__.st_id_for_deleting = st['id']

        assert st['score'] == score, f'Expected score is {score}'
        assert st['name'] == name, f'Expected name is {name}'


    @pytest.fixture
    def delete_student(self):
        yield
        if __class__.st_id_for_deleting:
            self.students_ctrl.delete_student(__class__.st_id_for_deleting)


