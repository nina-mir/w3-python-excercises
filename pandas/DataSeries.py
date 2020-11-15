import pandas as pd
import numpy as np

# 1. Write a Pandas program to create and display a one-dimensional array-like object containing an array of 
# data using Pandas module.

def prob_1(arr):
    return pd.Series(arr)

data = [10,20,"nina"]

print(prob_1(data))


index=["CA", "OZ", "MJ"]
john = pd.Series(data, index)

print(john)