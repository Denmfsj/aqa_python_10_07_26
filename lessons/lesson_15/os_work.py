import definitions
import os
from pathlib import Path

# .log


for items in os.walk(str(definitions.BASE_FOLDER)):

    cur_folder, list_of_folders, list_of_files = items

    for file_name in list_of_files:
        if file_name.endswith('.log'):
            print('LOG FILE FOUND: ', Path(cur_folder, file_name))


    # print(f'current dir ===> {cur_folder}')
    # print(f'dirs are  ===> {list_of_folders}')
    # print(f'files are ===> {list_of_files}')
    # print('-'*80)