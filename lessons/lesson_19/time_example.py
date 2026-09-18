import time


start_time = time.time()  # float, кількіасть ms з 1-1-70
print(start_time)
# time.sleep(1.5)  # чекати 1.5 секунди
print(time.time() - start_time)


loc_time = time.localtime()
print(loc_time)
print(loc_time.tm_wday, 'week day')
print(loc_time.tm_year, 'year')