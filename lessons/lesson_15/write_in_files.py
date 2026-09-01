import definitions
import os

# r, w, a
# rb, wb, ab
# r+, w+, a+
# rb+, wb+, ab+

file_for_testing = definitions.TEMP_FOLDER / 'file_for_writing'
definitions.TEMP_FOLDER.mkdir(exist_ok=True)

with open(file_for_testing, mode='w') as f:
    for items in os.walk(str(definitions.BASE_FOLDER)):

        cur_folder, list_of_folders, list_of_files = items

        f.write(f'current dir ===> {cur_folder}\n')
        f.write(f'dirs are  ===> {list_of_folders}\n')
        f.write(f'files are ===> {list_of_files}\n')
        f.write('-'*80)
        f.write('\n')
