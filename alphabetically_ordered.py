#Python Day 7, Assessment 2

"""Question:
Write a function that takes a string and returns it alphabetically ordered
"""
def alphabetric_str(inStr):
    words = [word.lower() for word in inStr.split()]
    # sort the list
    words.sort()
    
    print("The sorted words are:")
    for word in words:
       print(word)
       
alphabetric_str("Hello this Is an Example With cased letters")       
       
