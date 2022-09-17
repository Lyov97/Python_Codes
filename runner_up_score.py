#Python Day 5, Assessment 2

"""Question:
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given N scores. Store them in a list and find the score of the runner-up
"""
def runner_up_score():
    n = int(input())
    arr =list(map(int, input().split()))
    arr.sort()
    print(arr[(arr.index(max(arr)))-1])
    
runner_up_score()    
