import requests
from pygments.lexers import q

url = 'https://lms.ithillel.ua/assets/favicon/favicon-32x32.png'


data = requests.get(url)

print(data.content)

with open('image.png', 'wb') as f:
    f.write(data.content)