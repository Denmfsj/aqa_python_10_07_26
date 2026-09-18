from datetime import datetime
from tzlocal import get_localzone
import pytz

#
# client_time_dt = datetime.fromisoformat(some_time)
# local_tz = str(get_localzone())
# client_time_dt = pytz.timezone(local_tz).localize(some_time)

date_format_1 = '26-18-09T3:35:59.5487 PM'  #  UTC time
date_format_2 = '26-18-09T6:30:59.5487 PM +0900'  # + 9 hours to UTC time

format_1_dt = datetime.strptime(date_format_1, '%y-%d-%mT%I:%M:%S.%f %p')
format_2_dt = datetime.strptime(date_format_2, '%y-%d-%mT%I:%M:%S.%f %p %z')

local_tz = str(get_localzone())
format_1_with_tz_dt = pytz.timezone(local_tz).localize(format_1_dt)


print(format_1_with_tz_dt)
print(format_1_with_tz_dt < format_2_dt)
print(format_1_with_tz_dt - format_2_dt)

