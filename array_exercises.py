# 1. Write a Python program to create an array of 5 integers and display the array items. 
# Access individual element through indexes. Go to the editor
def prob_1():
    arr = []
    for i in range(5):
        arr.append(i*i)
    return arr

arr = prob_1()

print(arr[2], arr[4])
# 2. Write a Python program to append a new item to the end of the array. Go to the editor

