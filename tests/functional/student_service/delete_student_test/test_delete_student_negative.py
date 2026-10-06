from tests.functional.student_service.conftest import TestStudentsBase
import pytest




class TestDeleteStudentNegative(TestStudentsBase):


    @pytest.mark.parametrize('user_id', [
        'True',
        -10,
        [],
        15.4,
    ])
    def test_delete_user_negative(self, user_id):

        if user_id in (-10, [], 15.4):
            pytest.skip(reason='jira link: jira-XXXX')

        self.students_ctrl.put_student(
            st_id=user_id, user_data={},
            check_schema=False, expected_status_code=400)


