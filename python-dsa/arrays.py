# import array
from array import *
import numpy as np

#1 Create an array and traverse
arr = array('i', [1,2,3,4,5]) 
for i in arr: # O(N) because for loops = linear
    print(i)

#2 Acceses individual elements through indexes

first = arr[0]
print("first: ",  first)

#3 Append element to array
print(arr)
arr.append(6)
print(arr)

#4 Insert value in an array using insert()
arr.insert(3, 11)
print(arr)

#5 Extend python array using extend() method
arr1 = array('i', [10,11,12])
arr.extend(arr1)
print(arr)

#6 Add items from list into array using fromlist() method
list = [20, 21, 22]
arr.fromlist(list)
print(arr)

#7 Remove any array element using remove() method
arr.remove(22)
print(arr)

#8 Remove last array element using pop() method
arr.pop()
print(arr)

#9 Fetch any element through its index using index() method
print(arr.index(2))

#10 Reverse an array

arr.reverse()
print(arr)

# 11 Get array buffer information
arr.buffer_info()

#12 Check for number of occurences of an element using count() method
arr.append(11)
print(arr.count(11))
print(arr)

# Slice Elements from an array
print(arr[1:4])

# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return -1
#
# print(linear_search(arr, 8))
#
#
# arr.remove()
# print(arr)
# arr.insert(0,6)
# print(arr)


# def traverseArray(arr):
#     for i in arr:
#         print(i)
#
# traverseArray(arr)

# def accessElement(arr, index):
#     if index > len(arr):
#         print("index is not in arr")
#     else:
#         print(arr[index])
#
# accessElement(arr, 6)
