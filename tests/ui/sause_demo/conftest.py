import pytest

from utils.settings import d_settings


from playwright.sync_api import sync_playwright


browsers =[k for k in d_settings.browwsers_for_tests.split(',') if k]  # split по , виключаючі порожні строки

@pytest.fixture(params=browsers, scope='session')
def browser(request):
    with sync_playwright() as p:
        browser = getattr(p, request.param).launch(headless=True)
        # browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()