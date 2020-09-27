# 1. Write a Python program to calculate the length of a string. Go to the editor
def len_counter(str):
    count = 0
    for char in str:
        count += 1
    return count


# 2. Write a Python program to count the number of characters (character frequency) in a string. Go to the editor
# Sample String : google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

def char_frequency_counter(str):
    result = {}
    for char in str:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result
# 3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
# If the string length is less than 2, return instead of the empty string. Go to the editor
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String

def two_by_two_stringify(str):
    if len_counter(str) <= 2:
        return ''
    else: 
        return str[:2] + str[-2:]

# 4. Write a Python program to get a string from a given string where all occurrences of 
# its first char have been changed to '$', except the first char itself. Go to the editor
# Sample String : 'restart'
# Expected Result : 'resta$t'

def dollar_maker(str):
    str_changed = ''
    count = 0
    for char in str:
        if char == str[0] and count > 0:
            str_changed += '$'
        else:
            str_changed += char
        count += 1
    return str_changed

print(len_counter("google.com"))
print(len("google.com"))
print(char_frequency_counter("google.com"))
print(two_by_two_stringify("michael Jackson"))
print(two_by_two_stringify("donald trump"))
print(two_by_two_stringify("00"))
print(dollar_maker('nina'))

