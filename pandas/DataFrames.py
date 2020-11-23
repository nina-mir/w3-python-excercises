import pandas as pd
import numpy as np

# 1. Write a Pandas program to get the powers of an array values element-wise. Go to the editor
# Note: First array elements raised to powers from second array
# Sample data: {'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
# Expected Output:
# X Y Z
# 0 78 84 86
# 1 85 94 97
# 2 96 89 96
# 3 80 83 72
# 4 86 86 83

def prob_1(data):
    return pd.DataFrame(data)

print(prob_1({'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}))

# 2. Write a Pandas program to create and display a DataFrame from a specified dictionary data which has the index labels. Go to the editor
# Sample Python dictionary data and list labels:
# exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
# 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
# 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
# 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# Expected Output:
# attempts name qualify score
# a 1 Anastasia yes 12.5
# b 3 Dima no 9.0
# .... i 2 Kevin no 8.0
# j 1 Jonas yes 19.0

exam_data = {
'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],\
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],\
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],\
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

def prob_2(data, labels):
    return pd.DataFrame(data=data, index=labels)

print(prob_2(exam_data, labels))







