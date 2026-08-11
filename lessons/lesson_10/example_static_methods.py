from abc import abstractmethod
from datetime import datetime, timedelta


date_1 = '2025-10-10'
date_2 = '10-10-2025'

class DateTimeUtils:

    _JAPAN_DATA_FORMAT = "YYYY-mm-dd"
    _CLINET_X_DATE_FORMAT = "YYYY-mm-ddYHH:mm"

    @staticmethod
    def get_datetime_with_difference_in_days(n) -> datetime:
        return datetime.today() + timedelta(days=n)

    @classmethod
    def get_datetime_in_japan_format(cls, date_str) -> datetime:
        return datetime.strptime(date_str, cls._JAPAN_DATA_FORMAT)



yesterday = DateTimeUtils.get_datetime_with_difference_in_days(-1)
last_m = DateTimeUtils.get_datetime_with_difference_in_days(-30)


