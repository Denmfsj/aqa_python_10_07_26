# from .import_examples import greeting_version_lesson_16

import sys

from pathlib import Path

base_folder = Path(__file__).parent.parent.parent
sys.path.append(str(base_folder))
print(sys.path)

from lessons.lesson_16.import_examples import greeting_version_lesson_16

greeting_version_lesson_16('asdasd')
