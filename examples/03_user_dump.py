import json

user_dict = {
    "name": "John",
    "surname": "Williams",
    "age": 48,
    "city": "New York"
}

# serializing the sample dictionary to a JSON file
with open("03_user_dump.json", "w") as json_file:
    json.dump(user_dict, json_file)