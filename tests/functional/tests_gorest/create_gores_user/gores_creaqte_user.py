from tokenize import Token

import requests
import time
import json
from curlify import to_curl
url = 'https://gorest.co.in/public/v2/users'
TOKEN='ea1cf6a5c93238bfcd0c086b790f2353ff4418d899c26f8b9e8906a190c1111e'


base_body = {
    "name": "Avani Iyer",
    "email": f"asd2_{time.time()}@example.com",
    "gender": "female",
    "status": "active"
  }

headers = {'Authorization': f'Bearer {TOKEN}', 'User-Agent': 'aqa_test_hillel'}

response = requests.post(url=url, json=base_body, headers=headers)
curl = to_curl(response.request)
print(curl)
print(response.status_code)
response_json = response.json()
print(response_json)
print(response.headers)




# curl
# -H 'User-Agent: python-requests/2.34.2'
# -H 'Accept-Encoding: gzip, deflate'
# -H 'Accept: */*'
# -H 'Connection: keep-alive'
# -H 'Content-Length: 106'
# -H 'Content-Type: application/json'
# -d '{"name": "Avani Iyer", "email": "avani-'"'"'$(date +%s)'"'"'@example.com", "gender": "female", "status": "active"}'
# https://gorest.co.in/public/v2/usersuests/2.34.2'
