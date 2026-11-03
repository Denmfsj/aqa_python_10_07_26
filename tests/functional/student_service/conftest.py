import pytest
import allure
from allure_commons.types import LinkType

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
@allure.epic('Student service')
@allure.link('jira.com/TI-issue-id', link_type=LinkType.ISSUE)
@allure.link('jira.com/TI-test-case-id', link_type=LinkType.TEST_CASE)
@allure.link('jira.com/TI-link-id', link_type=LinkType.LINK)
@pytest.mark.skip(reason="jira.com/TI-546, investigate how to up server before tests run")
class TestStudentsBase:

    students_ctrl = StudentController()

