# 1. Write a Python program to find those numbers which are divisible 
# by 7 and multiple of 5, between 1500 and 2700 (both included). 

def prob_1(start, end):
    nl = []
    for i in range(start, end + 1):
        if i%35 == 0:
            nl.append(str(i))

    
    print(','.join(nl))

prob_1(0, 70)