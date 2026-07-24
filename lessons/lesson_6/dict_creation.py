

my_data = dict(name='Denys', age=35)

print(my_data)

my_new_dict = {
    1: 'some data',
    None: 'some_data',
    False: 'some_data',
    3.14: 'some_data',
    'str': 'some_data',
    (1,2): 'some_data',
    'str': 'some_data2'
}

print(my_new_dict)

my_new_dict['new_key'] = 'new_value'
my_new_dict[1] = [1,2,3]
# my_new_dict[[1,2,3]] = 1 - TypeError: unhashable type: 'list'

print(my_new_dict)

