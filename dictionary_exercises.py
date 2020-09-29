import operator

# 1. Write a Python script to sort (ascending and descending) a dictionary by value.

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

def sort_key_ascend_descend(d):
    ascend =  sorted(d.items(), key=operator.itemgetter(1)) 
    print("Ascending sort:", ascend)
    descend =  sorted(d.items(), key=operator.itemgetter(1), reverse=True) 
    print("Descending sort:", descend)

sort_key_ascend_descend(d)