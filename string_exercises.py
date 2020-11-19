import string

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

# 12. Write a Python program to count the occurrences of each word in a given sentence.

def word_counter(sentence):
    result = {}
    if sentence:
        # remove all the punctuations 
        sentence = sentence.translate(sentence.maketrans("","", string.punctuation))
        # tokenize by delimiter of space
        initial_list = sentence.split()
        for word in initial_list:
            count = initial_list.count(word)
            result[word] = count
        return result
    else:
        print("Enter a non-empty sentence")
        return result

# 13. Write a Python script that takes input from the user and displays 
# that input back in upper and lower cases.
def upper_unde_lower(text):
    print(text.upper(), text.lower())


upper_unde_lower("ich bin ein vogel im Himmel wie ein Kaese.")
print(word_counter("ich bin ein vogel im Himmel wie ein Kaese."))
print(word_counter(""))

# 14. Write a Python program that accepts a comma separated sequence of words 
# as input and prints the unique words in sorted form (alphanumerically). 
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white,red

def Q_14():
    items = input("Input comma separated sequence of words")
    initial_list = items.translate ( items.maketrans('', '', " ") ) 

    return initial_list.split(sep=',')

example = 'red, white, black, red, green, black'

# print ( sorted ( list ( set( Q_14() ) ) ) )

# 15. Write a Python function to create the HTML string with tags around the word(s). Go to the editor
# Sample function and result :
# add_tags('i', 'Python') -> '<i>Python</i>'
# add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'

def Q_15(tag_kind, sentence):
    text = '<{tag_kind}>{sentence}</{tag_kind}>'.format(tag_kind=tag_kind, sentence=sentence) 
    return text

def Q_15_1(tag, word):
    ''' Another solution '''
    return "<%s>%s</%s>" % (tag, word, tag)

print ( Q_15("i", "nina is great") )
print ( Q_15_1("a", "nina is great") )

# 17. Write a Python function to get a string made of 4 copies of the last two 
# characters of a specified string (length must be at least 2).
# Sample function and result :
# insert_end('Python') -> onononon
# insert_end('Exercises') -> eseseses

def Q_17(word):
    return word[-2:]*4

print(Q_17("betrachten"))

# 18. Write a Python function to get a string made of its first three characters of 
# a specified string. If the length of the string is less than 3 then return the original string. 
# Sample function and result :
# first_three('ipy') -> ipy
# first_three('python') -> pyt

def Q_18(word):
    if len(word) < 3:
        return word
    else:
        return word[:3]

print ( Q_18('Bau'))

# 19. Write a Python program to get the last part of a string before a specified character. Go to the editor
# https://www.w3resource.com/python-exercises
# https://www.w3resource.com/python


def Q_19(word, cutoff):
    count = 0
    for char in word:
        
        if char == cutoff:
            return word[: count]
        else:
            count += 1

def Q_19_find(word, cutoff):
    index = word.find(cutoff)
    if index > 0:
        print(index)
        return word[:index]
    else:
        return '{cutoff} is not a character in {word}'.format(cutoff=cutoff, word=word)

print( Q_19('https://www.w3resource.com/python-exercises', '-'))
print( Q_19_find('kompy', '-'))

# 20. Write a Python function to reverses a string if it's length is a multiple of 4. 
def Q_20(word):
    if len(word)%4 == 0:
        return ''.join(reversed(word))
        

print( Q_20("ninabona") ) 


# 21. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase
# characters in the first 4 characters.

def prob_21(word):
    counter = 0 
    for i in range(4):
        if word[i].isupper():
            counter += 1
    if counter >= 2:
        return word.upper()

print(prob_21('HOsitalee'))

# 22.Write a Python program to sort a string lexicographically.
print(sorted('HOsitalee', key=str.lower))
print(sorted('HOsitalee', key=str.upper))
result = ''.join(sorted('HOsitalee', key=str.lower))
print(result)

# 23. Write a Python program to remove a newline in Python.
def prob_23(sentence):
    # remove all the punctuations 
    sentence = sentence.translate(sentence.maketrans("","", "\n"))
    print(sentence)
   
    
str = """



        x
      nina


      """
print(str)
print("****")
prob_23(str)
# print(str)
