from pathlib import Path


# Path(__file__) - шлях до поточного файла /home/den/hillel/aqa_python_10_07_26/definition.py


BASE_FOLDER = Path(__file__).parent  # шлях до корня проекту
TEMP_FOLDER = BASE_FOLDER / 'temp'
# RESOURCES_FOLDER = BASE_FOLDER / 'tests' / 'resources'
RESOURCES_FOLDER = Path(BASE_FOLDER, 'tests', 'resources')
LIST_IDS_FILE_PATH = Path(RESOURCES_FOLDER, 'list_of_required_user_ids.txt')
