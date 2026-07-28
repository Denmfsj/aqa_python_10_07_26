import time
import random

#current_time = time.time()  # оттримати поточний час в mc стартучючі від 1.1.70

#print(time.time())
#time.sleep(2)  # заснути на 2 секунди
#print(time.time())

start_time = time.time()
expected_code = 200
time_between_requests = 0.5  # пів секунди
max_time_of_execution = 30

while True:  # вічно, поки не розірувуть через break

    # емітація запиту на сервер
    response_code = random.randint(180, 201)  # [180-200]

    print(f'response_code is {response_code}')
    if response_code == expected_code:
        break

    time.sleep(time_between_requests)

    current_time_of_execution = time.time() - start_time
    print(f'current_time_of_execution is {current_time_of_execution}')

    if current_time_of_execution > max_time_of_execution:
        print('Cant reach positive answer from server')
        break


