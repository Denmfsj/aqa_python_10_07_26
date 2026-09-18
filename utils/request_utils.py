import requests
import logging
from curlify import to_curl


class RequestUtls:

    logger = logging.getLogger(__name__)

    @classmethod
    def send_request(cls, method, url, **kwargs):

        cls.logger.info(f'Sending {method.upper()} request to {url}')

        response = requests.request(method, url, **kwargs)

        cls.logger.info(f'curl is')
        cls.logger.info(to_curl(response.request))
        cls.logger.info(f'status code is {response.status_code} request to {url}')

        return response

