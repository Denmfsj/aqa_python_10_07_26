# https://swapi.dev/api/people?search=re

import requests


url = 'https://swapi.dev/api/people/1'


users_response = requests.get(url=url) # послали запит через controller

# перевірили відповідь через marshmallow
# + додали в папку asseration файл з перевірками відповіді(height > 0, id співпадє з запитом, ....)
films_of_person =  users_response.json().get('films')

films_ids = [k.rstrip(r'/').split(r'/')[-1] for k in films_of_person]  # витягнули id

for f_id in films_ids:

    # get_film_info(f_id)  # послали запит і перевірили через controller + marshmallow
    # + додали в папку asseration файл з перевірками відповіді(id співпадє з запитом, ....)
    pass


