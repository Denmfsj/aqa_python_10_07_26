from tests.functional.student_service.update_student_test.conftest import UpdateStudentService


class TestUpdateStudentNegative(UpdateStudentService):


    def test_update_user_score_negative(self, create_and_delete_user):


        # !------------------------test------------------------!
        student = create_and_delete_user

        resp = self.students_ctrl.put_student(
            st_id=student['id'], user_data={},
            check_schema=False, expected_status_code=400)

        assert resp['message'] == 'You have to put name and/or score and/or score_name of the student'


