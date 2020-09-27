# 1. Write a Python program to calculate the length of a string. Go to the editor
def len_counter(str):
    count = 0
    for char in str:
        count += 1
    return count

print(len_counter("google.com"))
print(len("google.com"))
