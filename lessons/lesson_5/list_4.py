
csv_data = [
    ['id', 'name', 'age'],
    [1001, 'Den', 33],
    [1005, 'Alex', 37],
    [2004, 'Sofa', 30],
    [-1, '-', -1],
]

header, first_user, *rows, end_of_document = csv_data

print(header)
print(first_user)
print(rows)
print(end_of_document)


