#Day 17
#Assessment 1

pi=22/7
degree = float(input("Input degrees: "))
radian = degree*(pi/180)
print(radian)


#Assesment 2

def firstMissingPositive(A):
        m=max(A)
        ln=len(A)
        i=0
        while i<ln:
            if A[i]>=1 and A[i]<=ln:
                if A[A[i]-1]!=m+1:

                   A[A[i]-1], A[i] = m+1, A[A[i]-1]
                else:
                    i+=1

            else:
                i+=1
        for i in range(ln):
            if A[i]!=m+1:
                return i+1
