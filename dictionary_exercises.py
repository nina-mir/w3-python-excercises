import operator, random

# 1. Write a Python script to sort (ascending and descending) a dictionary by value.

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
d_1 = {'x': 10, 'y': 20, 'z': 30} 
list_1 = [x*x*x for x in range( 5)]
list_2 = [x*x for x in range(10, 20) if x%2 == 0]

example_1 = {'vater':0, 'mutter':1, 'bruder':1, 'schwester':1, 'onkel':2, 'tante':4, 'cousine': 10, 'cousin':10}

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
def add_key(new_key, dict):
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

# 5. Write a Python program to iterate over dictionaries using for loops. Go to the editor

def prob_5(d):
    print(type (d.items()) )
    print(d.items() )

    for key, val in d.items():
        print(str(key) + " -- " + str(val))

# 6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n)
#  in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

def prob_6(n):
    keys = [i for i in range(1, n +1)]
    values = [i*i for i in keys]
    return dict( zip(keys,values) )

def prob_6_dict_constructor(n):
    x = dict()
    for i in range(1, n + 1):
        x[i] = i*i
    return x


print(prob_6_dict_constructor(7))

# 7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys. Go to the editor
# Sample Dictionary
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
def prob_7():
    n =  random.randint(1, 15)
    return prob_6_dict_constructor(n)

print('{info}{dictionary}'.format(info='prob 7 output: ', dictionary=prob_7()))

# 8. Write a Python script to merge two Python dictionaries. 

def prob_8(*args):
    result = dict()
    for item in args:
        result = {**result, **item}
    return result

print(prob_8(d_1, example_1))

# 9. Write a Python program to iterate over dictionaries using for loops. 
def prob_9(*args):
    for item in args:
        for key, value in item.items():
            print('key is {key} and value is {value}'.format(key=key, value= value))



prob_9(example_1, d_1)

# 10. Write a Python program to sum all the items in a dictionary.
def prob_10(dict):
    return sum(dict.values())


print(prob_10(example_1))

# 11. Write a Python program to multiply all the items in a dictionary.
def prob_11(dict):
    result = 1
    for val in dict.values():
        result *= val
    return result

print(prob_11(d_1))

    
# 12. Write a Python program to remove a key from a dictionary.
def prob_12(dict, key=input):
    if key in dict:
        del dict[key]

print(example_1)
prob_12(example_1, key="nina")
print(example_1)

# 13. Write a Python program to map two lists into a dictionary.
def prob_13(list_1, list_2):
    return zip(list_1, list_2)

print(list_1)
print(list_2)
result = prob_13(list_1, list_2)
print(dict(result))