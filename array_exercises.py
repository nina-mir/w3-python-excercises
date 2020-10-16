from array import *


arr = [10, 20, 30, 40, 50, 'nina', 'vogel', 'nina', 'vogel', 'nina', 'vogel' ]
ar = array('i', [0,1,2,3,4])
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
