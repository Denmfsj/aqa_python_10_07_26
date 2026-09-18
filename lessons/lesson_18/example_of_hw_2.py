import requests
from curlify import to_curl

url = 'http://127.0.0.1:8080/upload'


with open('Screenshot.png', 'rb') as f:
    files_to_upload = {'image': f}

    # Виконання POST-запиту з файлом
    response = requests.post(url, files=files_to_upload)


print(response.status_code)
print(response.text)