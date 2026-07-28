
users = [
    {'id': 1, 'name': 'Den', 'age': 20, 'job': [{'id': 1, 'title': 'QA'}, {'id': 1, 'title': 'QA'}]},
    {'id': 2, 'name': 'Alex', 'age': 30},
    {'id': 3, 'name': 'Igor', 'age': 40, 'job': None},
    {'id': 4, 'name': 'Ivan', 'age': 50, 'job': [{'id': 2, 'title': 'CEO'}]},
    {'id': 5, 'name': 'Mor', 'age': 60, 'job': [{'id': 1, 'title': 'QA'}, {'id': 1, 'title': 'QA'}, {'id': 1, 'title': 'QA'}]},
    {'id': 6, 'name': 'Viktor', 'age': 70, 'job': [{'id': 3, 'title': 'Retired'}]},
    {'id': 7, 'name': 'Maria', 'age': 20, 'job': [{'id': 1, 'title': 'DevOps'}]},
    {'id': 8,  'age': 20, 'job': []},
]

users.sort(key=lambda user: user.get('age', 999))

user_by_name = sorted(users, key=lambda user: user.get('name', ''), reverse=True)
user_by_quantity_of_positions = sorted(
    users,
    #key=lambda user: len(user.get('job', []))  if user.get('job') is not None else 0,
    key=lambda user: len(user.get('job') or []),
reverse=True)

print(*user_by_quantity_of_positions, sep='\n')

# user_by_quantity_of_positions = sorted(
#     users, key=len, reverse=True)


# len(user.get('job') or [])  # bool(user.get('job')) == False ТО []
