from array import *


arr = [ 'nina', 'vogel', 'nina', 'vogel', 'nina', 'vogel' ]
ar = array('i', [0,1,2,3,4])
ar_2 = array('I', [88, 99, 77, 101])
example_list = [x for x in range(1,19)]
print(example_list)
# 1. Write a Python program to create an array of 5 integers and display the array items. 
# Access individual element through indexes. Go to the editor
def prob_1():
    arr = []
    for i in range(5):
        arr.append(i*i)
    return arr

# arr = prob_1()

# print(arr[2], arr[4])

# 2. Write a Python program to append a new item to the end of the array.

# 3. Write a Python program to reverse the order of the items in the array.

def prob_3(arr):
    arr.reverse()    
# prob_3(arr)

# 4. Write a Python program to get the length in bytes of one array item in the internal representation. 
def prob_4():
    arr = array('i', [1])
    print('unsigned int: ' + str(arr.itemsize))

prob_4()

# 5. Write a Python program to get the current memory address and the length 
# in elements of the buffer used to hold an array's contents and also find the 
# size of the memory buffer in bytes. Go to the editor

def prob_5(arr):
    buff = arr.buffer_info()
    print(buff, buff[1] * arr.itemsize)

prob_5(ar)

# 6. Write a Python program to get the number of occurrences of
#  a specified element in an array. Go to the editor

def prob_6(arr, item):
    return arr.count(item)

print(prob_6(arr, 'nina'))

# 7. Write a Python program to append items from inerrable to the end of the array.
def prob_7(addendum, arr):
    if type(arr) is ArrayType:
        return arr.extend(addendum)
    else:
        print("Nein! \n Nein! Nein!!!!   \n")

# prob_7([1,1000,30000], ar)
print(type(ar))
# print(arr)

# 8. Write a Python program to convert an array to an array of machine values and return the bytes representation.
def prob_8(arr):
    return bytes(arr)
# print(ar)
# print(prob_8(ar))

# 9. Write a Python program to append items from a specified list. Go to the editor
def prob_9(arr, list):
    arr.fromlist(list)
    
print(ar)
print(prob_9(ar, example_list))
print(ar)

# 10. Write a Python program to insert a new item before the second element in an existing array. Go to the editor
ar.insert(2,19999)
print(ar)

# 11. Write a Python program to remove a specified item using the index from an array. Go to the editor
ar.pop(2)
print(ar)

# 12. Write a Python program to remove the first occurrence of a specified element from an array.

def prob_12(arr, elem):
    arr.remove(elem)

