import pytest

from core.api.strudent_service.assertations.student_assertation import StudentAssertBase

import logging
import random

from tests.functional.student_service.conftest import TestStudentsBase
from utils.settings import d_settings

logger = logging.getLogger(__name__)



class TestGetStudent(TestStudentsBase):

    student_assert = StudentAssertBase()

    def get_random_student(self):

        response = self.students_ctrl.get_students(query_parameters={'limit': 100, 'sort_by': '-id'})

        ids = [s['id'] for s in response]  # витягую id студентів

        return random.choice(ids)

    @pytest.fixture(params=[10,20,50])
    def create_and_delete_test_students(self, request):
        score = request.param  # 10, 20, 50 в 3х тестах
        response = self.students_ctrl.post_student(user_data={
            "name": 'AQA_USER',
            "score": score,
        })
        yield response['id'], score

        self.students_ctrl.delete_student(response['id'])

    def test_get_created_student(self, create_and_delete_test_students):

        student_id, score = create_and_delete_test_students

        student = self.students_ctrl.get_student(student_id)
        assert student['name'] == 'AQA_USER'
        assert student['score'] == score


    @pytest.mark.parametrize('st_id', [1, 2, 1000, 'random'])
    def test_get_student(self, st_id):
        """Test get students"""

        student_id = self.get_random_student() if st_id == 'random' else st_id

        logger.info(f'\n!!!!-----\nrun test: getting one student(id={student_id}) and check:'
                    '\nall required fields are filled\n!!!!-----\n')

        student = self.students_ctrl.get_student(student_id)

        logger.info(student)

        self.student_assert.check_student_response_structure(student)