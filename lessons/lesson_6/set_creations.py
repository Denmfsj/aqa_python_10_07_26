set_of_els = {'str', 1, None, False, ('tuple', 'tuple')}

list_of_numbers = [1,2,3]

set_of_numbers = set(list_of_numbers)

set_of_numbers_sq = set()  # порожній сет можна створти тільки так, а не через {}
for number in range(50):  # від 0 до 49 ВКЛЮЧНО
    if number %2 != 0:  # не ділиться на 2
        set_of_numbers_sq.add(number**2)

print(set_of_numbers_sq)

set_compr = {number**2 for number in range(50) if number %2 != 0}

print(set_compr)