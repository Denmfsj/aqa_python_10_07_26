

api_response = (
    (0, 'Denys'),
    (1, 'Alex'),
    (2, 'Yur'),
    (3, ''),
    (4, None),
)


for user in api_response:
    print(user[1])  # response has structure [(user_id, user_name), (...), ...]

