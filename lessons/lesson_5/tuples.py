
my_names = ('Den', 'Alex', 'ololo', 'Olha', 'Yuri')  # немінний

print(my_names)

#print(my_names[0])  # Den
#print(my_names[3])  # Olha

#print(my_names[-1])  # Yuri
#print(my_names[-2])  # Olha


# print(my_names[999])  # error

print(my_names[1:4]) #  ('Alex', 'ololo', 'Olha') кожний  починаючі з індекса 1 вклчно по індекс 4 невключно
print(my_names[1:4:2])  # ('Alex', 'Olha') - кожний другий починаючі з індекса 1 вклчно по індекс 4 невключно





# @pytest.mark.parametrize('user_id',
#                          (1,2,3,4,5)
#                          )
# def test_age_is_more_than_18(user_id):

