import json

# some json example
example_json = '''
        {"menu": {
        "id": "file",
        "value": "File",
        "popup": {
            "menuitem": [
            {"value": "New", "onclick": "CreateNewDoc()"},
            {"value": "Open", "onclick": "OpenDoc()"},
            {"value": "Close", "onclick": "CloseDoc()"}
            ]
        }
        }}
    '''
# some JSON
x =  '{ "name":"John", "age":30, "city":"New York"}'


# 1. Write a Python program to convert JSON data to Python object. Go to the editor
def json_to_dict(j_obj):
    return json.loads(j_obj)



print(json_to_dict(example_json))
print(json_to_dict(x)['name'])