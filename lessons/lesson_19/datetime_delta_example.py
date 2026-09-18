from datetime import datetime, timedelta
from tzlocal import get_localzone
import pytz


date_format_1 = '26-18-09T3:35:59.5487 PM'  #  UTC time
date_format_2 = '26-18-08T6:30:59.5487 PM +0900'  # + 9 hours to UTC time

format_1_dt = datetime.strptime(date_format_1, '%y-%d-%mT%I:%M:%S.%f %p')
format_2_dt = datetime.strptime(date_format_2, '%y-%d-%mT%I:%M:%S.%f %p %z')

local_tz = str(get_localzone())
format_1_with_tz_dt = pytz.timezone(local_tz).localize(format_1_dt)


delta = format_1_with_tz_dt - format_2_dt

print(delta)
print(delta.days)
print(delta.seconds)
print(delta.total_seconds())
diff_in_hours = delta.total_seconds() / 60 / 60
print(round(diff_in_hours, 2))  # округлить знаки після коми до 2го знаку


print(datetime.now() + timedelta(hours=1, minutes=88, days=-5))



