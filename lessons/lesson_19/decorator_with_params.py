import time
import random


def retry(max_retries, error_type=Exception, delay: float|int =1):

    def decorator(func):
        def wrapper(*args, **kwargs):

            retries = 0
            while retries < max_retries:

                try:
                    return func(*args, **kwargs)
                except error_type as e:
                    print(f"Помилка: {e}. Повторна спроба {retries + 1}/{max_retries}")
                    retries += 1
                    time.sleep(delay)  # чекати delay секунд

            raise error_type("Досягнуто максимальну кількість спроб")

        return wrapper
    return decorator


@retry(max_retries=3, error_type=ConnectionError, delay=0.5)
def send_request_to_users():

    value = random.randint(1, 10)
    print(f'Value is {value}')

    if value < 4:
        raise ConnectionError('Cant connet to DB')

    if value < 6:
        raise AttributeError('Some unknown error')

    return 42

print(send_request_to_users())