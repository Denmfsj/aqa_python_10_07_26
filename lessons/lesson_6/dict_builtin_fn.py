
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

# my_data_copy = my_data.copy()
#
# # import copy
# # my_data_copy = copy.deepcopy(my_data)
#
# print(my_data)
# print(my_data_copy)
#
# print(id(my_data['work_info']))
# print(id(my_data_copy['work_info']))
#
# my_data['work_info']['new_key'] = 'new_value'
# print(my_data['work_info'])
# print(my_data_copy['work_info'])

# removed_el = my_data.pop('name')
# print(removed_el)
# print(my_data)
#
# random_el = my_data.popitem()
# print('random_el =', random_el)
# print(my_data)

my_data = {
    'id': 11,
    'name': 'Den',

    'work_info': {
        'id': 78,
        'position': None,
        # 'soft_skills': [{'id': 1, 'value': 'Funny'}],
        'skills': [
            {'id': 5, 'value': 'Python'},
            {'id': 8, 'value': 'git'}
        ]
    },
}

# my_data['work_info']['position'] = 'QA'

# if not my_data['work_info'].get('position'):  # bool(my_data['work_info'].get('position')) -> False
#     my_data['work_info']['position'] = 'QA'

if 'position' not in my_data['work_info']:
    my_data['work_info']['position'] = 'QA'

print(my_data['work_info'])