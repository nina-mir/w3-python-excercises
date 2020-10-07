sample_list = [x for x in range(10)]
sample_string_list = ['abc', 'xyz', 'aba', '1221']

# 1. Write a Python program to sum all the items in a list. Go to the editor
def sum_list(li):
    add = 0
    for item in li:
        add += item
    return add

# 5. Write a Python program to count the number of strings where the string length is 2 or more 
# and the first and last character are same from a given list of strings. Go to the editor
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

def prob_5(d):
    count = 0
    for item in d:
        if len(item) >= 2 and item[0]==item[-1]:
            count += 1
    return count


print(sum_list(sample_list))
print(prob_5(sample_string_list))
