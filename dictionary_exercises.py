import operator

# 1. Write a Python script to sort (ascending and descending) a dictionary by value.

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

def sort_key_ascend_descend(d):
    ascend =  sorted(d.items(), key=operator.itemgetter(1)) 
    print("Ascending sort:", ascend)
    descend =  sorted(d.items(), key=operator.itemgetter(1), reverse=True) 
    print("Descending sort:", descend)

# 2. Write a Python script to add a key to a dictionary. Go to the editor

def add_key_to_dict_obj(new_entry, dict):
    ''' new_entry must be a dictionary object '''
    dict.update(new_entry)
    return dict
# 2.1 To add a new key we can also do the following
def add_key(dict):
    new_item=2
    dict[new_key]=new_item
    # if we do this we do not have to pass the new_entry as a separate dictionary item into the arguments and we can dynamically change the item according to our needs.

# 3. Write a Python script to concatenate following dictionaries to create a new one. Go to the editor

# Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def dict_merg(*args):
    ''' funtion to merge multiple dictionaries '''
    merged_result = {}
    for item in args:
        merged_result.update(item)
    return merged_result

# 4. Write a Python script to check whether a given key already exists in a dictionary.

def key_exists(search, dict_obj):
    if search in dict_obj:
        print("Yes, it exists here!")
    else:
        print("NO, it is not there!")


# key_exists('nina', d)
sort_key_ascend_descend(d)
# print( add_key_to_dict_obj({'nina':38}, d)  ) 
# print(dict_merg(dic1, dic2, dic3))
