# from urllib import request
#
# list_of_numbers = [0, 1, 2, None, 0]
#
#
# for number in list_of_numbers:
#
#     try:
#         res = 10/number
#         print(f'The result is {res}')
#
#
#     except (TypeError, ZeroDivisionError) as e:
#         print(f'Cant work with {number}:   {e}')
#         raise e   # викликати помилку
#
#
#     except Exception as e:
#         print(f'Smth went wrong')
#
# print('Done')
#
# def send_request(user_id):
#     resposne = request.send(....)
#     resposne.raise_for_status()  # якщо сервер прислав помилку. то впаде
#     return resposne
#
#
# list_of_ids = [11,22,....]
#
# total_count = len(list_of_ids)
#
# for index, k in enumerate(list_of_ids, start=1):
#
#     if k in range(1, total_count, 100):
#         print(f'Done {index} percent')
#
#     try:
#         resposne = send_request(k)
#     except Exception:
#         continue
#
#     print(f'Data for {k} is available')
#     resposne.json()['name'] is not None   # словник
#
#
#
#
#
# # for number in list_of_numbers:
# #
# #     if not isinstance(number, (int, float)):
# #         print(f'Cant work with {number}')
# #         continue
# #
# #     if number == 0:
# #         print('You cant divide by 0')
# #         continue
# #
# #     print(10/number)