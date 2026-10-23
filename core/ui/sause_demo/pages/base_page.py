

class BasePage:


    def __init__(self, page, base_url):
        self.page = page
        self.base_url = base_url
        self.full_url = None


    def open(self):
        self.page.goto(f'{self.base_url}{self.full_url}')