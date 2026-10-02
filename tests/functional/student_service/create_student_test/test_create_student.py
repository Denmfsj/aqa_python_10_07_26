import random

from faker import Faker

from core.api.strudent_service.assertations.student_assertation import StudentAssertBase
from core.api.strudent_service.students_controller import StudentController

import logging


logger = logging.getLogger(__name__)
faker = Faker()



class TestCreateStudent:

    students_ctrl = StudentController()
    student_assert = StudentAssertBase()

    def test_create_user(self):

        name =  faker.name()
        score = random.choice(range(60, 100))

        st = self.students_ctrl.post_student(user_data={
            "name": name,
            "score": score,
        })

        self.student_assert.check_student_response_structure(st)

        assert st['score'] == score, f'Expected score is {score}'
        assert st['name'] == name, f'Expected name is {name}'


