[1,2,3,4]
{1,2,3,4,5,6,7}
{'key-1': 'value', 'key-2': 'value'}
'asdasdasdad'

my_data = {
    'id': 11,
    'name': 'Den',
    'position': 'AQA',
    'soft_skills': [{'id': 1, 'value': 'Funny'}],
    'skills': [
        {'id': 5, 'value': 'Python'},
        {'id': 8, 'value': 'git'}
    ]
}

for k in my_data.items():  # --> dictitems((key, value), (key2, value2))
    dict_key = k[0]
    dict_value = k[1]
    print(f'{dict_key} ==> {dict_value}')

    # print(f'{k[0]} ==> {k[1]}')

for dict_key, dict_value in [
    ('id', 1),
    ('name', 'Den'),
    ('position', 'AQA')
]:
    print(f'{dict_key} ==> {dict_value}')


for dict_key, dict_value in my_data.items():
    print(f'{dict_key} ==> {dict_value}')





# for k in my_data:
#     value = my_data[k]
#     print(f'{k} ==> {value}')
#
# for k in my_data.keys():
#     value = my_data[k]
#     print(f'{k} ==> {value}')

# for k in my_data.values():
#     print(k)

# separator = '-'*80
# new_number = 20
#
# new_number = 1
#
# for new_number in range(10):  # -> range(0,1,2,3,4,5,6,7,8,9)
#
#     print(f'^^3 of {new_number} is {new_number**3}')
#     print(separator)
#
# print(new_number)
