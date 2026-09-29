import requests
import logging

from curlify import to_curl

class RequestUtils:

    logger = logging.getLogger('RequestUtils')

    def send_request(self, method, path, params=None,
                     json=None, headers=None, expected_status_code=None, *args, **kwargs):

        if method.upper() == 'GET':
            response = requests.get(path, params=params, headers=headers)

        elif method.upper() == 'POST':
            response = requests.post(path, json=json, headers=headers)

        else:
            raise AttributeError(f'Method {method} not supported')

        self.logger.info(f'Sending request to {path} with {params}')

        curl_ = to_curl(response.request)
        self.logger.info(f'CURL: {curl_}')
        self.logger.info(f'status code is: {response.status_code}')


        if expected_status_code is not None:
            assert response.status_code == expected_status_code, \
                f'Get students returns status code {response.status_code} but should {expected_status_code}'

            return response