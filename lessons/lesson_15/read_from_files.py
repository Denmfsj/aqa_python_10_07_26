import definitions

# r, w, a
# rb, wb, ab
# r+, w+, a+
# rb+, wb+, ab+

with open(definitions.LIST_IDS_FILE_PATH, mode='r') as f:
    last_row = f.readlines()[-1]

print(last_row)

# with open(definitions.LIST_IDS_FILE_PATH, mode='r') as f:
#     for line in f:
#         print(line)
