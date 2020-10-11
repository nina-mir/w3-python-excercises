from array import *


arr = [10, 20, 30, 40, 50]

# 1. Write a Python program to create an array of 5 integers and display the array items. 
# Access individual element through indexes. Go to the editor
def prob_1():
    arr = []
    for i in range(5):
        arr.append(i*i)
    return arr

# arr = prob_1()

# print(arr[2], arr[4])

# 2. Write a Python program to append a new item to the end of the array. Go to the editor

# 3. Write a Python program to reverse the order of the items in the array. Go to the editor

def prob_3(arr):
    arr.reverse()    
prob_3(arr)

print(arr)

