users = [
    {'id': 1, 'name': 'Den', 'age': 20, 'job': [{'id': 1, 'title': 'QA'}]},
    {'id': 2, 'name': 'Alex', 'age': 30},
    {'id': 3, 'name': 'Igor', 'age': 40, 'job': None},
    {'id': 4, 'name': 'Ivan', 'age': 50, 'job': [{'id': 2, 'title': 'CEO'}]},
    {'id': 5, 'name': 'Mor', 'age': 60, 'job': [{'id': 1, 'title': 'QA'}]},
    {'id': 6, 'name': 'Viktor', 'age': 70, 'job': [{'id': 3, 'title': 'Retired'}]},
    {'id': 7, 'name': 'Maria', 'age': 20, 'job': [{'id': 1, 'title': 'DevOps'}]},
    {'id': 8, 'name': 'Anna', 'age': 20, 'job': []},
    {'id': 9, 'name': 'Olha', 'job': [{'id': 1, 'title': 'DevOps'}]},
]


# Надрукувати поточний список унікальних позицій для людей молодше 60

positions = []

for user in users:

    if user.get('age', 999) >= 60 :
        continue  # перейди на наступну ітерацію циклу

    if user.get('job') is None:
        continue


    # user['job'] -> [{'id': 1, 'title': 'QA'}]
    for position in user['job']:
        positions.append(position['title'])

    # positions.extend([k['title'] for k in user['job']])

print(set(positions))


# # Надрукувати поточний список унікальних позицій для людей молодше 60
#
# positions = []
#
# for user in users:
#
#     if user.get('age', 999) < 60 :
#
#         if user.get('job'):
#
#             # user['job'] -> [{'id': 1, 'title': 'QA'}]
#             for position in user['job']:
#
#                 positions.append(position['title'])



# print(set(positions))


# друкувати для кожного юзера його статус
# ok => age between 20 and 60
# warning = age > 60 or < 20
# error = no job
# for user in users:
#
#     if not user.get('job'): ## існує, ен погрожінй і не None
#         status = 'error'
#
#     elif user.get('age', 999) > 60 or user.get('age', 999) < 20:
#         status = 'warning'
#
#     else:
#         status = 'ok'
#
#     print(f'user_id = {user["id"]}, status is {status}')



    # if user['job'] and user['job'] is not None:
