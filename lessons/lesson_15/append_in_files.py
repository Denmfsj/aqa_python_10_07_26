import definitions
import os

# r, w, a
# rb, wb, ab
# r+, w+, a+
# rb+, wb+, ab+

file_for_testing = definitions.TEMP_FOLDER / 'file_for_appending.txt'
definitions.TEMP_FOLDER.mkdir(exist_ok=True)

with open(file_for_testing, mode='a') as f:

    f.write('second row\n')

