import json, operator

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

python_obj = {
  'name': 'David',
  'class':'I',
  'age': 6  
}

# 1. Write a Python program to convert JSON data to Python object. Go to the editor
def json_to_dict(j_obj):
    return json.loads(j_obj)

# 2. Write a Python program to convert Python object to JSON data. Go to the editor
def dict_2_json(dict):
    return json.dumps(dict)

# 4. Write a Python program to convert Python dictionary object (sort by key) to JSON data. 
# Print the object members with indent level 4. 

def sort_dict_then_2_json(d):
    d_sorted = sorted(d.items(), key=operator.itemgetter(0))
    return json.dumps(d_sorted, indent=4)
#OR another solution:

print(json.dumps(python_obj, sort_keys=True ,indent=4))




print(sort_dict_then_2_json(python_obj))
# print(json_to_dict(example_json))
# print(json_to_dict(x)['name'])
# output = dict_2_json(python_obj)
# print(type(python_obj))
# print(type(output))
# print(output)

