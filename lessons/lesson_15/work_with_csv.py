import definitions
import csv


file_for_testing = definitions.TEMP_FOLDER / 'output.csv'


with open(file_for_testing) as f:

    data = list(csv.reader(f))

# print('headers: ', data[0])

headers = data[0]
body = data[1:]

future_csv_as_a_dict = []

# for row in body:
#
#     tuple_of_2_els = zip(headers, row)
#     dict_as_a_row = dict(tuple_of_2_els)
#     future_csv_as_a_dict.append(dict_as_a_row)
# print(future_csv_as_a_dict)

cvs_as_a_dict = [dict(zip(headers, row)) for row in body]
print(cvs_as_a_dict)

new_file_data = []
new_file_data.append(headers)



for row in cvs_as_a_dict:
    # print(f'{row.get("Name")} is living in {row.get("City")}')
    new_row = [row.get("Name"), row.get("City"), -111]
    new_file_data.append(new_row)

with open(str(definitions.TEMP_FOLDER / 'new_file.csv'), 'w') as f:
    writer = csv.writer(f)
    writer.writerows(new_file_data)
