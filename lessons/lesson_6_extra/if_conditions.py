card_number = 111555
cvv = 123
has_money = True

# True and True -> True
# True and False -> False
# True or False - > True
# False or False -> False
# not True -> False
# not False -> True

check_card_number = 111555
check_cvv = 122

# if card_number == check_card_number and cvv == check_cvv and has_money:
#     print('You have access to your account')
# else:
#     if not has_money:
#         print('You have no money')
#     else:
#         if cvv != check_cvv:
#             print('Incorrect cvv')
#         else:
#             print('Incorrect card number')


if card_number == check_card_number and cvv == check_cvv and has_money:
    print('You have access to your account')
elif not has_money:
    print('You have no money')
elif cvv != check_cvv:
    print('Incorrect cvv')
else:
    print('Incorrect card number')



# api_response = [{'id': 1}, {'id': 2}, {'id': 3}]
# # api_response = []
#
# if api_response and api_response[0]['id'] is not None:  # and,  or  -> булева алгебра
#     print('user 1 is exist and id is not None')



# if has_money is True:  # if bool(has_money is True)
#     print('You have smth')
#
# if has_money:  # if bool(has_money)
#     print('You have smth')
#
# if has_money is False:
#     print('You have no money')
#
# if not has_money:  # not True --> False
#     print('You have no money')



