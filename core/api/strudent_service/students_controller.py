import requests
import logging
from curlify import to_curl


from core.api.strudent_service.DTOs.output.student_schema import StudentSchema
from utils.settings import d_settings

from core.utils.request_utils import RequestUtils

logger = logging.getLogger(__name__)


class StudentController(RequestUtils):
    """надсилати запити по вказаним ендпоінтам

    get students
    get students/st_id
    post students/
    put students/st_id
    delete students/st_id

    post /auth/

    """

    def __init__(self, base_url=d_settings.STUDENTS_URL):
        self.auth_value = None
        self.base_url = base_url


    def __set_auth_value(self):
        self.auth_value = self.get_token()

    def get_token(self, expected_status_code=200):
        response = self.send_request(
            method='POST',
            path=f'{self.base_url}/auth/',
            json={'name': d_settings.STUDENTS_USER_NAME,
                  'password': d_settings.STUDENTS_USER_PWD},  # login, password
            expected_status_code=expected_status_code)

        return response.text

    def dz_auth(self, ):
        from requests.auth import HTTPBasicAuth
        response = requests.post(auth=HTTPBasicAuth('test_user', 'test_pass') )
        return response.json()


    def get_students(self, query_parameters=None, expected_status_code=200,
                     check_schema=True):

        response = self.send_request(method='GET', path=f'{self.base_url}/students',
                          params=query_parameters, expected_status_code=expected_status_code)

        if check_schema:
            StudentSchema(many=True).load(response.json())

        return response.json()


    def get_student(self, student_id: int, query_parameters=None, expected_status_code=200,
                    check_schema=True):


        response = self.send_request(method='GET', path=f'{self.base_url}/students/{student_id}',
                          params=query_parameters, expected_status_code=expected_status_code)

        if check_schema:
            StudentSchema().load(response.json())

        return response.json()


    def post_student(self, user_data: dict, expected_status_code=201,
                     set_auth=True, check_schema=True):

        if self.auth_value is None:
            self.__set_auth_value()

        response = self.send_request(
            method='POST', path=f'{self.base_url}/students/',
            headers={'token': self.auth_value} if set_auth else {},
            json=user_data, expected_status_code=expected_status_code)

        if check_schema:
            StudentSchema().load(response.json())

        return response.json()


    def put_student(self, st_id: int, user_data: dict, expected_status_code=200,
                     set_auth=True, check_schema=True):

        if self.auth_value is None:
            self.__set_auth_value()

        response = self.send_request(
            method='PUT', path=f'{self.base_url}/students/{st_id}',
            headers={'token': self.auth_value} if set_auth else {},
            json=user_data, expected_status_code=expected_status_code)

        if check_schema:
            StudentSchema().load(response.json())

        return response.json()


    def delete_student(self, st_id: int, expected_status_code=204,
                     set_auth=True):

        if self.auth_value is None:
            self.__set_auth_value()

        response = self.send_request(
            method='DELETE', path=f'{self.base_url}/students/{st_id}',
            headers={'token': self.auth_value} if set_auth else {},
            expected_status_code=expected_status_code)

        return response.text
