'''
Created on 24-May-2020

@author: sasidharl
'''

if __name__ == '__main__':
    pass
# A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
fruits = {"apple", "banana"}

print("print set values : ", fruits)  # Sets are unordered, so you cannot be sure in which order the items will appear.

# print("print set values : ",fruits[0])

# use for loop to print values 
for x in fruits:
    print(" print one by one from set : ", x)
    
# verify the value is exist in the set or not
print("banana" in fruits)  # it will print boolean value 
# Set is a Case sensitive and not allow the duplicate values

print("Banana" in fruits)  # it will print boolean value

# add item in the set
fruits.add("orange")
print("----", fruits)
# Add multiple items to a set, using the update() method:

fruits.update(['mango', 'Cherri', 'grapes'])
print("----", fruits)

# get the length of set
print(len(fruits))

# To remove an item in a set, use the remove(), or the discard() method.
fruits.remove("banana")
print(len(fruits))

fruits.discard("mango")
print(len(fruits))
fruits.discard("mango")  # item to remove does not exist, discard() will NOT raise an error.
print("*********", len(fruits))
    
# pop() method will remove the last item from the set, here you dont know which item will be removed because set is an unordered
print(fruits)
fruits.pop()
print(fruits)

# join two sets
set1 = {1,2,3}
set2 = {"name", "surname"}
print("&&&&&&&&&&", set1, set2)

#use union method to join two sets
set3 = set1.union(set2)
print("used union method to join two sets : ", set3)

# update() method inserts the items in set2 into set1:
set4 = {4,5,6}
set3.update(set4)
print(set3)

# clear() method will make an empty list
print("<<<<<<<<<",fruits)
# fruits.clear()
print(fruits)

# del keyword will delete the set completely.
del fruits

# print(fruits)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)
print(x, y )
print(z)

a = x.intersection(y)

print(a)

#Return True if all items set x are present in set y:
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
b = x.issubset(y)

print(b)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

#Return a set that contains all items from both sets, except items that are present in both sets:
z = x.symmetric_difference(y)
print("xxxxxxxx : ", x)
print("xxxxxxxx : ", y)
print("xxxxxxxxxxx",z)