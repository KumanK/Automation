import jsonschema
from jsonschema import validate

schema = {
    "type": "object",
    "properties": {
        "price": {"type": "number","val":34},
        "name": {"type": "string"},
    },
}

print(validate(instance={"name" : "Eggs", "price" : 34.99}, schema=schema))
# print(validate(instance={"name" : "Eggs", "price" : 'k'}, schema=schema))

