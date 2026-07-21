my_friends_list = ['Alex', 'John', 'Michael']

print(id(my_friends_list), my_friends_list)

list_of_ages = [18,25,66]

my_friends_list.append('Olha')  # додае елемент в кінець

print(id(my_friends_list), my_friends_list)

my_friends_list.append(list_of_ages)
my_friends_list.extend(list_of_ages)
print(id(my_friends_list), my_friends_list)

print(my_friends_list[-4])  # res of append
print(my_friends_list[-3])  # 18  -res of extend




