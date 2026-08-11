

def is_odd_and_less_30(num):
    if num >= 30:
        return False

    if num % 2 == 0:
        return False

    return True

list_of_numbers = list(range(11, 84))  # "список" чисел

filtered_list_of_numbers = list(filter(is_odd_and_less_30, list_of_numbers))  # Як фільтрувати, що фільтрувати
print(list_of_numbers)
print(filtered_list_of_numbers)


manual_filtered_numbers = []
for k in list_of_numbers:
    if is_odd_and_less_30(k):
        manual_filtered_numbers.append(k)

filtered_list_of_numbers = list(filter(is_odd_and_less_30, list_of_numbers))


def set_min_30_max_100(number):

    if number < 30:
        return 30
    if number > 100:
        return 100
    return number


# map -
list_of_numbers = list(range(-10, 40))

list_updated_numbers = list(map(set_min_30_max_100, list_of_numbers))
print(list_updated_numbers)


def set_number_in_pow(number, number_2):

    return number ** number_2

list_updated_numbers = list(map(set_number_in_pow, [5,6,7], [8,9,55]))
print(list_updated_numbers)


print(dict(zip(['a', 'b', 'c'], [1, 2, 3, 5, 6, 7])))

# isinstance, type, min, max
