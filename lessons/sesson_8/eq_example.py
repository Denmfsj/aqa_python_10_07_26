

class BaseUser:

    def __eq__(self, other):  # __eq__ --> ==

        if self.id_ != other.id_:
            return False
        if self.name != other.name:
            return False
        if self.age != other.age:
            return False
        return True


class ApiUser(BaseUser):

    def __init__(self, id_, name, age, was_online_in_hors):
        self.id_ = id_
        self.name = name
        self.age = age
        self.was_online_in_hors = was_online_in_hors


    def __str__(self):
        return f'ApiUser: {self.id_} | {self.name} | {self.age} | {self.was_online_in_hors}'

class DbUser(BaseUser):

    def __init__(self, id_, name, age, las_login_date):
        self.id_ = id_
        self.name = name
        self.age = age
        self.las_login_date = las_login_date

    def __str__(self):
        return f'DbUser: {self.id_} | {self.name} | {self.age} | {self.las_login_date}'


# api_resp = {'id': 1, 'name': 'Alex', 'age': 25, 'was_online_in_hors': 5}
# db_data = {'id': 1, 'name': 'Alex', 'age': 25, 'las_login_date': '2026-01-01'}

#api_resp = ApiUser.__init__(id_=1, name='Alex', age=25, was_online_in_hors=5)

api_resp = ApiUser(**{'id_': 1, 'name': 'Alex', 'age': 25, 'was_online_in_hors': 5})
db_data = DbUser(**{'id_': 1, 'name': 'Alex', 'age': 25, 'las_login_date': '2026-01-01'})


print(api_resp)
print(db_data)

print(f'are they Equal?: {api_resp == db_data}')  # --> api_resp.__eq__(db_data)
print(f'are they Equal?: {db_data == api_resp}')  # --> db_data.__eq__(api_resp)


