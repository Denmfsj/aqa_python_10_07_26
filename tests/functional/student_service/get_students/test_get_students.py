import pytest

from core.api.strudent_service.assertations.student_assertation import StudentAssertBase
from core.api.strudent_service.students_controller import StudentController
from assertpy import assert_that

import logging

logger = logging.getLogger(__name__)



class TestGetStudents:

    students_ctrl = StudentController()
    student_assert = StudentAssertBase()


    def test_get_students(self):
        """Test get students"""

        logger.info('\n!!!!-----\nrun test: getting first users and check: \nnumber of users = 10'
                    '\nall required fields are filled\n!!!!-----\n')

        students = self.students_ctrl.get_students()

        assert len(students) == 10

        for st in students:
            self.student_assert.check_student_response_structure(st)


    @pytest.mark.parametrize('sort_by',
                             ['id', '-id', 'name', '-name', 'score',
                              '-score', 'updated_date', '-updated_date'])
    def test_students_sort_by_check(self, sort_by):
        logger.info(f'\n!!!!-----\nrun test: getting students sorted by {sort_by} '
                    'and check sorting\n!!!!-----\n')

        students = self.students_ctrl.get_students(query_parameters={'sort_by': sort_by})
        self.student_assert.check_students_is_sorted_by_parameter(students, sort_by)