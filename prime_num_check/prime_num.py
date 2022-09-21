#Day 11, Assasment 2
'''question: Write a function that will receive a natural number N and return True if it is prime, otherwise it will return False ''

def prime_num_check(num):

        for i in range(2, int(num/2)+1):
            
            if (num % i) == 0:
                print(False)
                break
        else:
            print(True)
    
        
        
prime_num_check(5)
prime_num_check(4)
prime_num_check(1)
