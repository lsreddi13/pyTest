'''
Created on 23-May-2020

@author: sasidharl
'''

if __name__ == '__main__':
    pass

# Task1 : Print "Technologies" from the given string
str1 = 'Hello i am from Pramati Technologies, i live in Hyderabad'
# print(str1)
# a = str1.rindex("Technologies")
print(str1[24:36])

#Task2 : Print list items in reverse order from the mentioned value or index.
temperatures = [38.6, 42.3, 40, 30, 39.0, 35, 55, 27, 42]
# print(temperatures)

xy = temperatures[2:-4 ]
xy.reverse()
print(xy)

#Task3 : Print only keys
school = { "Jagadish" : 1256, "Vamshi" : 1444, "Satish" : 1324, "Kiran" : 1564}
print(school.keys())
