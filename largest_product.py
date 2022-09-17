#Python Day 5, Assessment 1

"""Question:
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.
"""
def maxProduct(arr, n):
 
    # Sort the array
    arr.sort()
    num1 = num2 = 0
 
    # Calculate product of two smallest numbers
    sum1 = arr[0] * arr[1]
 
    # Calculate product of two largest numbers
    sum2 = arr[n - 1] * arr[n - 2]
 
    # Print the pairs whose product is greater
    if (sum1 > sum2):
        num1 = arr[0]
        num2 = arr[1]
    else:
        num1 = arr[n - 2]
        num2 = arr[n - 1]
    print("Max product pair = {", num1, ",", num2, "}", sep="")
 
# Driver Code
arr = [1, 4, 3, 6, 7, 0]
n = len(arr)
 
maxProduct(arr, n)
