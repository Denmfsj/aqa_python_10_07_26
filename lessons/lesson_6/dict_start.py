my_data = {
    'id': 11,
    'name': 'Den',

    'work_info': {
        'id': 78,
        'position': 'AQA',
        # 'soft_skills': [{'id': 1, 'value': 'Funny'}],
        'skills': [
            {'id': 5, 'value': 'Python'},
            {'id': 8, 'value': 'git'}
        ]
    },
}

# print(my_data['second name'])  # KeyError: 'second name'

second_name = my_data.get('second_name')
if second_name is None:
    print('There is no second name')
print(my_data.get('second_name'))  # None по замовчуванню

soft_skills = my_data['work_info'].get('soft_skills', []) # => []]

quantity_of_soft_skills = len(soft_skills)
quantity_of_skills = len(my_data['work_info']['skills'])
print('quantity_of_skills =', quantity_of_skills)
print('quantity_of_soft_skills =', quantity_of_soft_skills)

#
# print(my_data['name'])  # 'Den'
# print(my_data['work_info'])  # -> dict  {'id': 78, 'position': 'AQA', 'skills': [{'id': 5, 'value': 'Python'}, {'id': 8, 'value': 'git'}]}
# print(my_data['work_info']['position'])  # -> AQA
# print(my_data['work_info']['skills'][1]['value'])  # -> git

# skill_of_id_8 = [k['value'] for k in my_data['work_info']['skills'] if k['id'] == 8]
# print(skill_of_id_8)


