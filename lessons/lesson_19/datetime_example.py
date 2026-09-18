from datetime import datetime

# print(datetime.today())

date_format_1 = '2026-09-18 18:35:59'  # iso format
date_format_2 = '18-09-2026 18:35:59'
date_format_3 = '09-18-2026 18:35:59'   # US
date_format_4 = '26-18-09 6:35:59 PM'  # y, d, m
date_format_5 = '26-18-09T6:35:59.5487 PM +0900'  # y, d, m
date_format_6 = '26.18.09 6PM'  # custom format   y.d.m hPM


format_1_dt = datetime.strptime(date_format_1, '%Y-%m-%d %H:%M:%S')
format_2_dt = datetime.strptime(date_format_2, '%d-%m-%Y %H:%M:%S')
format_3_dt = datetime.strptime(date_format_3, '%m-%d-%Y %H:%M:%S')
format_4_dt = datetime.strptime(date_format_4, '%y-%d-%m %I:%M:%S %p')
format_5_dt = datetime.strptime(date_format_5, '%y-%d-%mT%I:%M:%S.%f %p %z')
format_6_dt = datetime.strptime(date_format_6, '%y.%d.%m %I%p')





print(format_1_dt)
print(format_2_dt)
print(format_3_dt)
print(format_4_dt)
print(format_5_dt)
print(format_6_dt)

