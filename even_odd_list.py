#Python Day 7, Assessment 1

"""Question:
Provided is a list of numbers. For each of the numbers in the list, determine whether they are 
even. If the number is even, add True to a new list called is_even. If the number is odd, then 
add False. 
"""
#Version 1

def even_odd(lst):
    is_even = []
    for X in lst:
        if (X % 2 == 0):
            is_even.append(True)
        else:
            is_even.append(False)
        X+=1
    return is_even        
    
    
print(even_odd([8,11,4,7,9,85,22]))
