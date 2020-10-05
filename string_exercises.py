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

# 5. Write a Python program to get a single string from two given strings, separated by a space 
# and swap the first two characters of each string. Go to the editor
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

def char_mixup(str_1,str_2):
    if len(str_1)>=2 and len(str_2) >= 2:
        return str_2[0:2]+str_1[2:] + ' ' + str_1[0:2]+str_2[2:]
    else:
        return ''

# 7. Write a Python program to find the first appearance of the substring 'not' and 'poor'
# from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. 
# Return the resulting string. Go to the editor
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

def not_poor_finder(str):
    position_not  = str.find('not')
    position_poor = str.find('poor')
    if (position_not and position_poor) and (position_not < position_poor):
        return str[0:position_not] + 'good'
    else:
        return '' 
# 8. Write a Python function that takes a list of words and returns the length of the longest one. 

def find_longest_word(words_list):
    length = 0
    for word in words_list:
        if len(word) > length:
            length = len(word)
    return length

# 9. Write a Python program to remove the nth index character from a nonempty string. lowest n is 1.
def delete_nth_char(n, str):
    index = 0
    new_str = ''
    if str:
        for c in str:
            index += 1
            if index == n:
                pass
            else:
                new_str = new_str + c
        return new_str
    else:
        return "Empty strings needs to operations!"

# 10. Write a Python program to change a given string to a new string where the first and last chars 
# have been exchanged.
# w3 solution :       return str1[-1:] + str1[1:-1] + str1[:1]    
def first_last_exchange(str):
    try:
        first = str[0]
        last = str[-1]
        new_list = []
        new_str = ''
        
        for c in str:
            new_list.append(c)
        
        new_list[0] = last
        new_list[-1] = first
    
        for c in new_list:
            new_str += c
        return new_str 
    except:
        return 'Did you really pass a non-empty string?!'

# 11. Write a Python program to remove the characters which have odd index values 
# of a given string. Go to the editor

def rm_odd_index(str):
    new_str = ''
    for i in range(len(str)):
        if i % 2 == 0:
            new_str += str[i]
    return new_str


# print(delete_nth_char(1, 'nina'))
# print(delete_nth_char(1, ''))
# print(first_last_exchange(''))
print( rm_odd_index('Verfassen')) 

# print(len_counter("google.com"))
# print(len("google.com"))
# print(char_frequency_counter("google.com"))
# print(two_by_two_stringify("michael Jackson"))
# print(two_by_two_stringify("donald trump"))
# print(two_by_two_stringify("00"))
# print(dollar_maker('nina'))
# print(char_mixup('Sweden','Ziemlich'))
# print(not_poor_finder('The lyrics is not that poor!'))
# print(find_longest_word(["PHP", "Exercises", "Backend"]))