import pytest

from core.api.strudent_service.assertations.student_assertation import StudentAssertBase
from core.api.strudent_service.students_controller import StudentController

import logging
import random

logger = logging.getLogger(__name__)



class TestGetStudent:

    students_ctrl = StudentController()
    student_assert = StudentAssertBase()

    def get_random_student(self):

        response = self.students_ctrl.get_students(query_parameters={'limit': 100, 'sort_by': '-id'})

        ids = [s['id'] for s in response]  # витягую id студентів

        return random.choice(ids)


    @pytest.mark.parametrize('st_id', [1, 2, 1000, 'random'])
    def test_get_student(self, st_id):
        """Test get students"""

        student_id = self.get_random_student() if st_id == 'random' else st_id

        logger.info(f'\n!!!!-----\nrun test: getting one student(id={student_id}) and check:'
                    '\nall required fields are filled\n!!!!-----\n')

        student = self.students_ctrl.get_student(student_id)

        self.student_assert.check_student_response_structure(student)