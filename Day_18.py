#Day 18
#Assesment 1

def seacrh(text,word) :
    if word in text :
        print ('Word found')
    else:
        print('Word not found')

text = input()
word = input()
seacrh(text,word)


#Assessment 2

def seperator(num):    
    res = '{:,}'.format(num)
    if num > 0:
        print(res)
    else:
        print("negative")
           
        
seperator(1000000)   
