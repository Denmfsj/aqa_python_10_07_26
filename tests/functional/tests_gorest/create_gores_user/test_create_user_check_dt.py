import requests
from curlify import to_curl
import time
from datetime import datetime
import pytz
from tzlocal import get_localzone
from utils.datetime_utils import DateTimeUtils
from utils.request_utils import RequestUtls


url = 'https://gorest.co.in/public/v2/users'
TOKEN='ea1cf6a5c93238bfcd0c086b790f2353ff4418d899c26f8b9e8906a190c1111e'


base_body = {
    "name": "Avani Iyer",
    "email": f"asd2_{time.time()}@example.com",
    "gender": "female",
    "status": "active"
  }

headers = {'Authorization': f'Bearer {TOKEN}', 'User-Agent': 'aqa_test_hillel'}




def test_user_created_check_time_of_creation():

    start_dtime = DateTimeUtils.get_dt_now_with_tz()
    time.sleep(1)
    response = RequestUtls.send_request(method='post', url=url, json=base_body, headers=headers)
    time.sleep(1)
    end_dtime = DateTimeUtils.get_dt_now_with_tz()

    r_headers = dict(response.headers)
    date_of_creation = r_headers['Date']
    date_of_creation_dt = DateTimeUtils().convert_gorest_str_headers_time_to_dt_with_tz(date_of_creation)

    diff_with_end_time = max(end_dtime, date_of_creation_dt) - min(date_of_creation_dt, end_dtime)
    diff_with_start_time = max(start_dtime, date_of_creation_dt) - min(date_of_creation_dt, start_dtime)

    error_msg = f'Date time is not between {start_dtime} <= {date_of_creation_dt} <= {end_dtime}'
    assert date_of_creation_dt < end_dtime, error_msg + f' the diff is {diff_with_end_time}'
    assert date_of_creation_dt > start_dtime, error_msg + f' the diff is {diff_with_start_time}'

