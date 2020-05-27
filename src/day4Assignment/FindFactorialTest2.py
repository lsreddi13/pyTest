'''
Created on 27-May-2020

@author: sasidharl
'''
from ast import Num
num = int(input("Enter a number: "))  
factorial = 1  
if num < 0:  
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    print("this is factorial", num*(num-1))
    
    for i in range(1,num + 1):
        factorial = factorial*i  
    print("The factorial of",num,"is",factorial)  