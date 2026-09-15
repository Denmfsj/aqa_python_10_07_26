# https://swapi.dev/api/people?search=re

import requests


url = 'https://swapi.dev/api/people'


users_response = requests.get(url=url)

print('object', users_response)
print('status_code', users_response.status_code)
print('text', users_response.text)
print('json', users_response.json())  # json.loads(users_response.text)
print('count of users', users_response.json().get('count'))  # json.loads(users_response.text).get('count')