#Python Day 9, Assessment 2
'''Question:
Write a program which accepts a sequence of comma-separated numbers from the console and
generates a list and a tuple which contains every number.
'''

def num_sequence():
    numbers = input("Type in numbers seperated only by a comma :")
    numbers_split = numbers.split(',') #list
    
    number_tuple = tuple(numbers_split) #tuple

    print((number_tuple))
    print(numbers_split)
    
num_sequence()
