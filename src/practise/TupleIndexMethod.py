'''
Created on 24-May-2020

@author: sasidharl
'''

if __name__ == '__main__':
    pass

# Search for the first occurrence of the value 8, and return its position:
tuple1 = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = tuple1.index(5)

print(x)

tuple2 = ("sasi", "shannu", "prem", "chinni", "sasi")
y = tuple2.index("sasi")
print(y)


#The index() method raises an exception if the value is not found.