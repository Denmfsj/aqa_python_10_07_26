import random

import pytest
from faker import Faker

import logging

from tests.functional.student_service.conftest import TestStudentsBase

logger = logging.getLogger(__name__)
faker = Faker()




class UpdateStudentService(TestStudentsBase):

    @pytest.fixture(scope="class")
    def create_and_delete_user(self):
        # !------------------------pre-condition------------------------!
        name =  faker.name()
        score = random.choice(range(60, 100))

        st = self.students_ctrl.post_student(user_data={
            "name": name,
            "score": score,
        })

        yield st

        # !------------------------post-condition------------------------!
        self.students_ctrl.delete_student(st_id=st['id'])