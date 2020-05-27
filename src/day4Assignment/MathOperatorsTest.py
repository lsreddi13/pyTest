'''
Created on 27-May-2020

@author: sasidharl
'''




a = 6
b = 5
print(a is b)



a = 70
b = 60

if a >50 and b >50:
    print("a and b are greater than 50")
elif a<50 and b>50:
    print("a is lessthan 50 and b is greater than 50")
elif a>50 and b<50:
    print("a is greater than 50 and b is lessthan 50")
else:
    print("a and b lessthan 50")


if a >50 or b >50:
    print("1. atleast one value is big")
elif a<50 or b>50:
    print("2. atleast one value is big")
elif a>50 or b<50:
    print("3. atleast one value is big")
else:
    print("4. No value is big")
    
    
    