#Python Day 7, Assessment 1
#Match given 2 list elements 

def match(list1,list2):
    print("list1 items:\n",list1)
    print("list2 items:\n",list2)
    
    list3 = [element for element in list1 if element in list2]
    
    print("Common Elements in list1 and list2: ",list3)

match(([4,2,82,11,5,7, 8,14]),([5,2,22,8,5,11,1]))  
