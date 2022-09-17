#Python Day 9, Assessment 1

"""Question:
With a given integral number n, write a program to generate a dictionary that contains (i, i*i)
such that is an integral number between 1 and n (both included). and then the program should
print the dictionary. """
#Version 1

def generate_dictionary():

n=int(input())
d=dict()
for i in range(1,n+1):
    d[i]=i*i

print(d)
generate_dictionary()

#Version 2
def gen_dicto():

num=int(input("Enter a number:"))
dicto={x:x*x for x in range(1,num+1)}
print(dicto)
gen_dicto()
