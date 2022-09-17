#Python Day 8, Assessment 2

"""Question:
Get the user to enter some text and print out True if it’s a palindrome, False otherwise. 
"""

def isPalindrome(input_string):
 

    # Using predefined function to
    # reverse to string print(input_string)

    rev = ''.join(reversed(input_string))
 
    # Checking if both string are
    # equal or not
    
    if (input_string == rev):
        return True
    return False
 
# main function
def in_word(string):
    ans = isPalindrome(string)
    
    if (ans):
        print(True)
    else:
        print(False)
        
in_word("kayak")
in_word("word")
        
