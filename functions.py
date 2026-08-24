import logging
from core.utils.logger_utils import internal_function_logger

def factorial(n: int):

    logging.info(f'Factorial: input number is {n}')

    logging.debug(f'Comparing with < 0')
    if n < 0:
        raise ValueError(f'You have to use 0 or positive numbers. You put {n}')

    logging.debug(f'checking type')
    if type(n) != int:
        raise TypeError(f'Only int allowed, you put {type(n)}')

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def is_anagram(word1: str, word2: str):
    """
    description
    """
    return sorted(word1) == sorted(word2)


def filter_even_numbers(lst: list[int|float]):
    return [num for num in lst if num % 2 == 0]


def find_primes(n: int) -> list:

    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


def triangle_area(a: int|float, b: int|float, c: int|float):
    # if a + b <= c or a + c <= b or b + c <= a:
    #     return 0
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area


def convert_to_24_hour(time_str: str):

    internal_function_logger.info(f'Star executing convert_to_24_hour with {time_str}')

    if type(time_str) == list:
        internal_function_logger.critical(f'Value {time_str} TypeError')
        raise TypeError

    if type(time_str) == dict:
        internal_function_logger.critical(f'Value {time_str} ValueError')
        raise ValueError


    internal_function_logger.debug(f'Value {time_str} has no ValueError or TypeError')

    parts = time_str.split()

    internal_function_logger.info(f'parts are {parts}')

    if len(parts) != 2:
        raise ValueError('Time format is not a `hh:mm period`')
    time, period = parts
    hours, minutes = map(int, time.split(':'))
    if period.lower() == 'pm' and hours != 12:
        hours += 12
    elif period.lower() == 'am' and hours == 12:
        hours = 0

    internal_function_logger.info(f'return {hours:02}:{minutes:02}')

    return f'{hours:02}:{minutes:02}'