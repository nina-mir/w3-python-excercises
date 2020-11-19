import pandas as pd
import numpy as np

# 1. Write a Pandas program to create and display a one-dimensional array-like object containing an array of 
# data using Pandas module.

def prob_1(arr):
    return pd.Series(arr)

data = [10,20,"nina"]

print(prob_1(data))


index=["CA", "OZ", "MJ"]
john = pd.Series(data, index, name='john')

print(john)

# 2. Write a Pandas program to convert a Panda module Series to Python list and it's type. 
print(john.to_markdown())
print(john.to_list())

# 3. Write a Pandas program to add, subtract, multiple and divide two Pandas Series.
# Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]

def prob_3(list_1, list_2, operator):
    series_1 = pd.Series(list_1, name = 'first')
    series_2 = pd.Series(list_2, name = 'second')
    if operator == '+':
        return series_1 + series_2
    elif operator == '-':
        return series_1 - series_2
    elif operator == '*':
        return series_1 * series_2
    else:
        return series_2 / series_2

print( prob_3([2, 4, 6, 8, 10], [1, 3, 5, 7, 9], '/'))