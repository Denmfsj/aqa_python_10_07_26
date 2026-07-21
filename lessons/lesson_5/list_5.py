
user_ids = [1,2,5,6,3,4,99,8,6,7]


# user_ids.sort(reverse=False)  # ми змінили цей список
user_ids.sort()  # ми змінили цей список
print(user_ids)  # сортування по замовчуванню від меншого до більшого

user_ids.sort(reverse=True) # сортування  від більшого до меншого
print(user_ids)


user_names = ['Alex', 'Yr', 'Sofia', 'Olha', '&*', '1', 'alex']  # &*, 1', A, a,
print(id(user_names), 'id of names')
user_names.sort()
print(user_names)
print(id(user_names), 'id of names')

user_names.sort(reverse=True)
print(user_names)

# combined_list = ['Alex', 33, '15']
# combined_list.sort(reverse=True)

user_ids = [1,2,5,6,3,4,99,8,6,7]
print(id(user_ids), 'id of user_ids')

sorted_list_of_ids = sorted(user_ids)  # НЕ міняє user_ids
print(id(user_ids), 'id of user_ids')
print(id(sorted_list_of_ids), 'id of sorted_list_of_ids')

sorted_list_of_ids_reversed = sorted(user_ids, reverse=True)  # НЕ міняє user_ids
print(user_ids)
print(sorted_list_of_ids)
print(sorted_list_of_ids_reversed)

[1,2,'asddfa'].sort()