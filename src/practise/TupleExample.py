'''
Created on 24-May-2020

@author: sasidharl
Tuple - examples

'''

if __name__ == '__main__':
    pass

# declare tuple
a = ("apple", "banana", "watermelon")


#
print("a length : ",len(a))
# print all values from tuple
print(a)

# print value by index
print(a[1])

#print value by negative index
# -1 refers the last item in the index
print(a[-1])

# -2 refers the second last item
print(a[-2])

#declare 2 tuples at a time in single line.
# we can create tuple with the combination of integer and string types.
tuple1, tuple2 = (123, 'xyz', 'zara'), (456, 'abc')
print ("First tuple length : ", len(tuple1))
print ("Second tuple length : ", len(tuple2))

print(tuple1[0])

#convert tuple to list
x = ("apple", "banana", "cherry")
print(x)
y = list(x)
#change the  value by index in the list
y[1] = "kiwi"
x = tuple(y)
print(x)

# You cannot add items to a tuple:
# remove item in tuple
#join two tuples

# tuple constructor

#count

# index
