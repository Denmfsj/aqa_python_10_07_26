from datetime import datetime, timedelta
import pytz
from tzlocal import get_localzone


class DateTimeUtils:

    jp_str_format = '%Y-%m-%d %H:%M:%S'
    gorest_header_format = '%a, %d %b %Y %H:%M:%S %Z'


    def convert_gorest_str_headers_time_to_dt_with_tz(self, str_time) -> datetime:
        date_of_creation_dt = datetime.strptime(str_time, self.gorest_header_format)   # dt object
        return pytz.timezone('UTC').localize(date_of_creation_dt)

    @staticmethod
    def get_dt_now_with_tz() -> datetime:
        return pytz.timezone(str(get_localzone())).localize(datetime.now())

    def convert_jp_to_dt(self, dt_string) -> datetime:
        return datetime.strptime(dt_string, self.jp_str_format)

    @staticmethod
    def convert_iso_str_to_dt(dt_string):
        return datetime.isoformat(dt_string)

    @staticmethod
    def get_yesterday():
        return datetime.today() - timedelta(days=1)


    @staticmethod
    def get_date_with_delta(**kwargs):
        return datetime.today() + timedelta(**kwargs)


    @staticmethod
    def get_current_quarter():
        m = datetime.today().month

        if m in (12,1,2):
            return 1

        elif m in (3,4, 5):
            return 2

        elif m in (6,7, 8):
            return 3

        else:
            return 4

