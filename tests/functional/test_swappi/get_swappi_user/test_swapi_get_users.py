# https://swapi.dev/api/people?search=re

import requests
import pytest
import logging

from assertpy import soft_assertions, assert_that

logging.basicConfig(level=logging.INFO)
url = 'https://swapi.dev/api/people'



def test_swapi_get_users_smoke():

    response = requests.get(url)
    assert response.status_code == 200, f'Response from  {url} return {response.status_code} status code'



@pytest.mark.parametrize('q_params', [
    {'search': 're', 'page': 1},
    {'search': 'Leia', 'page': 1},
    {'search': 'asd', 'page': 1},
], ids=['search re', 'search Leia', 'search asd'])
def test_swapi_get_search(q_params):

    search_ph = q_params['search']

    logging.info(f'Sending request to {url} with {q_params}')

    response = requests.get(url, params=q_params)
    logging.info(f'Status code is {response.status_code}')

    assert response.status_code == 200, f'Response from  {url} return {response.status_code} status code'

    response_json = response.json()

    logging.info(f'Response contains {response_json["count"]} items')

    with soft_assertions():
        for user in response_json['results']:

            assert_that(user['name'],
                        f'{user["name"]} does not have {search_ph}').contains(search_ph)


