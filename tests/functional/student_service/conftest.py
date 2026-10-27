import pytest

from core.api.strudent_service.students_controller import StudentController



# function - default
# class - виконується 1 раз для всіх тестів в class
# module - виконується 1 раз для всіх тестів в file
# package - виконується 1 раз для всіх тестів в package
# session - виконується 1 раз для всіх тестів

# @pytest.fixture(scope="session")
# def students_ctrl():
#     yield StudentController()


@pytest.mark.api
class TestStudentsBase:

    students_ctrl = StudentController()

