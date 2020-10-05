sample_list = [x for x in range(10)]

# 1. Write a Python program to sum all the items in a list. Go to the editor
def sum_list(li):
    add = 0
    for item in li:
        add += item
    return add

print(sum_list(sample_list))
