#Python Day 10, Problem 2

'''Question: 
Напишите программу, которая выводит чётные числа из заданного списка и
останавливается, если встречает число 616.
'''

def black_number():

    num = input().split(' ')
    
    for i in num:
    
       if int(i) == 616:
    
           break;
    
       elif int(i)%2 == 0:
    
           print(i)
           
black_number()           
