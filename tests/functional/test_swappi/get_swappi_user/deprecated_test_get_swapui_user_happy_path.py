from core.api.user_service.controller.swagger_ctrl import SwapiCtrl
from assertpy import assert_that

# from core.api import SwapiCtrl


def test_swappi_happy_path():

    user_id = 555
    resp = SwapiCtrl().get_swappi_by_user_id(user_id)
    assert_that([1,2,3, None, 5]).is_sorted()