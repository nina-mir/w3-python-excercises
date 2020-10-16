import operator, copy

sample_list = [x for x in range(10)]
string_list = ['abc', 'xyz', 'aba', '1221', 'aba', 'nina', 'nina']
xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


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

# 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple 
# from a given list of non-empty tuples. 
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

def prob_6(list):
   #  method.1 using lambda functions
   sorted_1 = sorted(list,  key= lambda item: item[1] )
   #  method.2 using operator.itemgetter
   sorted_2 = sorted(list,  key= operator.itemgetter(1) ) 
   return sorted_2
    
# 7. Write a Python program to remove duplicates from a list. 
def prob_7(li):
    set_temp = set(li)
    return list(set_temp)

# 8. Write a Python program to check a list is empty or not. Go to the editor
def prob_8(li):
    if not li:
        print("empty")
    else: 
        print("not empty")


# 9. Write a Python program to clone or copy a list
def prob_9_list_constructor(original):
    #shallow copy 
    return list(original)

def prob_9_slice(original):
    # Shallow copy
    return original[:]

def prob_9_extend(original, clone):
    #Shallow copy
    clone.extend(original)

def prob_9_copy_shallow(original):
    #Shallow copy
    return copy.copy(original) 

def prob_9_copy_deep(original):
    #Deep copy
    return copy.deepcopy(original) 

# clone.extend(xs)
clone = prob_9_copy_deep(xs)
clone[0] = 'Giles'

print("original" + str(xs))
print("clone" + str(clone))
xs[1][0] = "captain"
print("original" + str(xs))
print("clone" + str(clone))

# prob_8([1, "nina"])

# print(string_list)
# output = prob_7(string_list)
# print(output)


# print(prob_6([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
# print(sum_list(sample_list))
# print(prob_5(sample_string_list))
