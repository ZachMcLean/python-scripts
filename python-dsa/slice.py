# slice operator is : 
# [from : to] (but not including)

myList = ['a', 'b', 'c','d','e','f']

print(myList[0:6])
# you can omit the first element if you want to start from beginning of list
print(myList[:6])
# same if you omit 2nd element
print(myList[4:])
# omitting both elements will include all elements in the list
print(myList[:])
