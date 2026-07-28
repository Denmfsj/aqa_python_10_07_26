users = [
    {'id': 1, 'name': 'Den', 'age': 20, 'job': [{'id': 1, 'title': 'QA'},
                                                {'id': 12, 'title': 'AQA'}]},
    {'id': 2, 'name': 'Alex', 'age': 30},
    {'id': 3, 'name': 'Igor', 'age': 40, 'job': [{'id': 12, 'title': 'AQA'}]},
]

# Надрукувати хоч одну позицію
for user in users:

    need_to_break = False

    if user.get('age', 999) >= 60 :
        continue  # перейди на наступну ітерацію циклу

    if user.get('job') is None:
        continue

    for position in user['job']:
        print(position['title'])
        need_to_break = True

        break  # розірвати цикл

    if need_to_break:
        break

    print('take next user')

print('Done')