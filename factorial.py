#Python Assessments_12, problem 1
'''Question: The factorial of a number N is the product 1 × 2 × ... × N. Notation: N!.
Given a natural N, compute the value of N!. It is forbidden to use the library math in this
problem.'''


def fact(num):
    if num==1:
        f=1
    else:
        f = num * fact(num-1)
    return f

print(fact(3))
print(fact(6))
print(fact(10))

