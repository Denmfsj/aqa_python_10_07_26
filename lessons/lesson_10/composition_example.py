

class LessonPageLocator:

    LECTOR_SCORE = '....'
    LESSON_NAME = '....'



class LessonPage(BasePage):

    def __init__(self, driver):
        self.locators = LessonPageLocator()

    def get_lesson_name(self):

        return self.driver.get(self.locators.LECTOR_SCORE)
