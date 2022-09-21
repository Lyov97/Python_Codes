#Python Day 13, Problem 2

'''Question:
 Write function to print fibonacci series. In the line of calling function try use "input number" method.
'''


def fibonacci_series(num):
    a = 0
    b = 1
    print(a,b,end=" ")
    while(num-2):
        c=a+b
        a,b = b,c
        print(c,end=" ")
        num=num-1
        

fibonacci_series(int(input("Enter the number of terms in the sequence: ")))        
