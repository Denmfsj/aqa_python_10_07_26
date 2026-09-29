from faker import Faker

from core.api.strudent_service.assertations.student_assertation import StudentAssertBase
from core.api.strudent_service.students_controller import StudentController

import logging


logger = logging.getLogger(__name__)
faker = Faker()



class TestCreateStudent:

    students_ctrl = StudentController()
    student_assert = StudentAssertBase()

    def test_create_user_smoke(self):

        self.students_ctrl.post_student(user_data={
            "name": faker.name(),
            "score": 95,
        })
