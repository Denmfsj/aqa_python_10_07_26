


# def user_friends(*friends, beast_friend='Nobody'):  # *args
#
#     print(f'best_friend is {beast_friend}')
#
#     for k in friends:  # friends = tuple
#         print(f'Friend is {k}')
#
#
# user_friends('Den', 'Alex', 'Yur', beast_friend='Sofa')
# #user_friends('Den', 'Alex', 'Yur')
#
# print(1,2,4,6,'asdasdasdas','asdas', sep=' | ', end='\nthis is the end')


# def url_logger(url, *users,  **query_params):  # *args, **kwarg
def url_logger(url, *args,  **kwargs):  # *args, **kwarg

    print(f'Sending request to {url}')
    print(f'with parameters: {kwargs}')  # qwery_params = dict
    print(f'this request is available for {args}')  #  users = tuple


url_logger('http://....com',
           'Den', 'Alex', 'Ihor',
           language='en', sort_by='-date')
