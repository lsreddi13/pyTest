'''
Created on 24-May-2020

@author: sasidharl
'''

if __name__ == '__main__':
    pass

#  lists are written with square brackets. and allow duplicates.
list1 = ["apple", "banana", "cherry","banana", "cherry"]
print(list1)


# access the item from the list - access the list items by referring to the index number:
#print values by index.
list_fruits = ["apple", "banana", "cherry","mango", "chicku", "pinapple", "grapes"]
print(list_fruits[3])

# Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.
print(list_fruits[-1])
#Print the last third item of the list:
print(list_fruits[-3])
# Range of index - range of indexes by specifying where to start and where to end the range.
print(list_fruits)
#The search will start at index 1 (included) and end at index 3 (not included).
print(list_fruits[1:3])

print(list_fruits)
#print all values from index 3 ( include the mentioned index value )
print(list_fruits[3:])

#print all values before index 3 ( exclude the mentioned index value )
print(list_fruits[:3])


#  returns all items except last two items
print(list_fruits[:-2])

#  returns the last two items  
print(list_fruits[-2:])

#add items in the list
list_fruits.append("orange")

print("fruits : ", list_fruits)

# add an item at the specified index, use the insert() method:
list_fruits.insert(1,"mapple")

print("fruits : ",list_fruits)


#remove an item from the list with value name
list_fruits.remove("mapple")
print("fruits : ",list_fruits)

# remove the last item from the lsit
print("----fruits : ",list_fruits)
list_fruits.pop()
print("----fruits : ",list_fruits)

# del keyword removes the specified index:
print("+++++ fruits : ",list_fruits)
del list_fruits[1]
print("+++++ fruits : ",list_fruits)



# clear method will make an empty list
list_fruits.clear()
#delete the complete list
del list_fruits
# print("+++++ fruits : ",list_fruits)

# copy the list into another list
list_names = ["Sasi", "Shannu", "Prem"]
print("list : ", list_names)
names = list_names.copy() # by using the copy method
print("new list copied existing list : ", names)

name_list = list(names)
print("by using list method : ", name_list)

# join two lists
gents = ["Sasi", "Shanu", "Prem", "goutham"]
ladies = ["chini", "tulasi", "jyothi", "purna"]

# several ways to join, or concatenate, two or more lists in Python.
# by using the + operator.

family = gents + ladies
print(family)
print("------",gents + ladies)

# join two lists are by appending all the items from list2 into list1, one by one:
list1 = [1, 2, 3]
list2 = [4, 5,6]
for x in list2:
    list1.append(x)
    
print(list1, "kkkkkkkkk")

#extend() method to add list4 at the end of list3:
list3 = ["a", "b" , "c"]
list4 = [1, 2, 3]

list3.extend(list4)
print("extend method to add two lists : ",list3)

# list() constructor to make a new list.
list5 = list(list3)
print("constructor list ro make new list : ",list5)
# this is set, even if we have duplicate it won;t display.
# set1 = {"apple", "banana", "cherry","banana", "cherry"}
# print(set1)

##########################33
# append()    Adds an element at the end of the list
# clear()    Removes all the elements from the list
# copy()    Returns a copy of the list
# count()    Returns the number of elements with the specified value
# extend()    Add the elements of a list (or any iterable), to the end of the current list
# index()    Returns the index of the first element with the specified value
# insert()    Adds an element at the specified position
# pop()    Removes the element at the specified position
# remove()    Removes the item with the specified value
# reverse()    Reverses the order of the list
# sort()    Sorts the list