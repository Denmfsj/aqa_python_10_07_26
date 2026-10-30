import json
from playwright.sync_api import sync_playwright, Page
from pytest import fixture

@fixture(scope='session')
def page():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        yield page
        browser.close()


def test_mocking_swagger(page: Page):


    mock_data = {
        "swagger": "2.0",
        "info": {
            "title": "Mocked Petstore - IT WORKS!",
            "version": "9.9.9",
            "description": "Цей опис згенеровано локально для перевірки моку."
        },
        "paths": {}
    }


    request_intercepted = []

    def handle_route(route):
        request_intercepted.append(True)
        print("\n[MOCK] Запит перехоплено! Відправляємо кастомні дані...")
        route.fulfill(
            status=200,
            content_type="application/json",
            body=json.dumps(mock_data)
        )


    page.route("**/v2/swagger.json", handle_route)
    page.goto("https://petstore.swagger.io")

    cookie_button = page.locator("text='Allow all cookies'") # або селектор вашого банера
    if cookie_button.is_visible(timeout=3000):
        cookie_button.click()

    page.wait_for_selector(".info h1", timeout=10000)

    header_text = page.locator(".info h1").inner_text()
    print(f"[UI] Текст на сторінці: '{header_text}'")
