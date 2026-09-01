import definitions
import json


definitions.TEMP_FOLDER.mkdir(parents=True, exist_ok=True)

data = (
    { "name": "John", "age": 30, "city": "New York"},
    { "name": "Alex", "age": `asd`, "city": "New York"},
    { "name": "Sofia", "age": True, "city": "New York"}
)

# json_obj = json.dumps(data, indent=4)
# print(data)
# print(json_obj, type(json_obj))
#
# reverted_json = json.loads(json_obj)
# print(reverted_json, type(reverted_json))

json_d = definitions.TEMP_FOLDER / 'dumps_json_obj.json'

with open(json_d, 'w') as f:
    json.dump(data, f, indent=2)


with open(json_d) as f:
    readable_json = json.load(f)

print(readable_json)
print(readable_json[-1])

