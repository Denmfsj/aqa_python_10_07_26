
# not mutable
my_name = 'Denys'  # str
my_age = 34 # int
my_temp = 36.6 # float
is_alive = True  # True or False
None  # нічого
my_tuple = ('Alex', 'Ihor')  # tuple, кортеж





# mutable
my_friends = ['Alex', 'Ihor']  # list
my_info = {
    'Name': 'Denys',
    'age': 33
}  # dict
my_subj = {'math', 'lith'}  # set, множина


my_name = 'Denys'  # 137686282593760
my_first_name = my_name  # 137686282593760

#print(id(my_name), my_name)
##print(id(my_first_name), my_first_name)
#my_name = my_name + ' Mer'
#print(id(my_name), my_name)
#print(id(my_first_name), my_first_name)

my_enemies = my_friends

print(id(my_friends), my_friends)
print(id(my_enemies), my_enemies)

my_friends.append('Ivan')
my_enemies.remove('Ihor')

print(id(my_friends), my_friends)
print(id(my_enemies), my_enemies)

