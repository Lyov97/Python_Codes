# Sum_Python
# Sum of  given Numbers using while loop in Python

print("Hello world")

def sum_for_you(num):

    sum=0
    while (num!=0):
        sum=sum+(num%10)
        num=num//10

    return sum
    
print(sum_for_you(12345))
