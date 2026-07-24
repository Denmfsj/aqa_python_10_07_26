from urllib import request

True
False

age_more_18 = True

my_age = 33

has_income = False

# my_age >= 18 => True

if my_age >= 18:  # if bool(my_age >= 18 ==> True) == bool(True) ==> True
    print('you can buy beer')

# if my_age >= 18 and my_age <= 65:  # bool(my_age >= 18)  AND bool(my_age <= 65) ==> True and True => True
#     print('You have to pay taxes')


# AND OR

if (my_age >= 18 and my_age <= 65) and  has_income:  # True and False => False
    print('You have to pay taxes')


# url = '...'
#
# response = request.get(url)  # послати запит кудись
#
# if response.response_time > 10 and 'user_info' not in url:  # sec
#     log.warnign('Response takes too long time')

# if age_more_18:  # if bool(condition) == True
#     print('you can bye beer')


# bool([]) -> False, бо список порожній
# bool([1,2]) -> True, бо список НЕ порожній

print('em,pty objects')
print(bool([]))
print(bool({}))
print(bool(tuple()))
print(bool(set()))
print(bool(''))
print(bool(0))
print(bool(False))
print(bool(None))

print('NON empty objects')

print(bool([1,2]))
print(bool({1,2}))
print(bool({1:2}))
print(bool(True))
print(bool(1))
print(bool(3.14))
print(bool(-200))
print(bool('a'))


print('real projects')

users_from_api = []

if users_from_api:  # bool(users_from_api)
    print('Start..')
else:
    print('The list is empty')