import requests
import logging
from curlify import to_curl

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

    def __init__(self):
        self.auth_value = None


    def __set_auth_value(self):
        self.auth_value = self.get_token()

    def get_token(self, expected_status_code=200):
        response = self.send_request(
            method='POST',
            path=f'http://127.0.0.1:8081/auth/',
            json={'name': 'test', 'password': 'test'},
            expected_status_code=expected_status_code)

        return response.text


    def get_students(self, query_parameters=None, expected_status_code=200):

        response = self.send_request(method='GET', path='http://127.0.0.1:8081/students',
                          params=query_parameters, expected_status_code=expected_status_code)

        return response.json()


    def get_student(self, student_id: int, query_parameters=None, expected_status_code=200):


        response = self.send_request(method='GET', path=f'http://127.0.0.1:8081/students/{student_id}',
                          params=query_parameters, expected_status_code=expected_status_code)

        return response.json()


    def post_student(self, user_data: dict, expected_status_code=201, set_auth=True):

        if self.auth_value is None:
            self.__set_auth_value()

        response = self.send_request(
            method='POST', path=f'http://127.0.0.1:8081/students/',
            headers={'token': self.auth_value} if set_auth else {},
            json=user_data, expected_status_code=expected_status_code)

        return response.json()
