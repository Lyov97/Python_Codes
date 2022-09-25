#Python Day 10, Problem 1

'''Question: 
Напишите программу, которая принимает имя файла и выводит его расширение. Если расширение у файла определить невозможно, выросите исключение.
'''


def lengthOfLastWord(s):
    i, length = len(s) -1, 0
    while s[i] == ' ':
        i-= 1
    while i >= 0 and s[i] != ' ':
        length += 1
        i-= 1
    return length


print(lengthOfLastWord("agsjhag agfsga gjfas"))
