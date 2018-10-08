import json

with open("test_data.json") as file:
    datastore = json.load(file)
    print(datastore["temperature49"])
    print(datastore)