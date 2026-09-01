import definitions
import shutil

print(definitions.TEMP_FOLDER)


future_folders = definitions.TEMP_FOLDER / 'folder_1' / 'folder_x'

print(future_folders)
print(future_folders.exists())
future_folders.mkdir(parents=True, exist_ok=True)
print(future_folders.exists())

shutil.rmtree(definitions.TEMP_FOLDER)