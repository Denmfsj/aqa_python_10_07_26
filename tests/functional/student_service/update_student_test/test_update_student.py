from tests.functional.student_service.update_student_test.conftest import UpdateStudentService


class TestUpdateStudent(UpdateStudentService):

    def test_update_user_score(self, create_and_delete_user):

        # створити студента <---- pre- condition
        # оновити студента  <---- test
        # видалити студента <---- post- condition

        # !------------------------test------------------------!
        student = create_and_delete_user

        upd_st = self.students_ctrl.put_student(
            st_id=student['id'], user_data={
                "score": 10,
            })

        assert upd_st['score'] == 10, 'Score of updates st must be 10'



    def test_update_user_name(self, create_and_delete_user):


        # !------------------------test------------------------!
        student = create_and_delete_user

        upd_st = self.students_ctrl.put_student(
            st_id=student['id'], user_data={
                "name": 'Test_name',
            })

        assert upd_st['name'] == 'Test_name', 'Name of updates st must be Test_name'

