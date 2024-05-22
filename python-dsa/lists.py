ints = [1,2,3,4]
print(ints)
strs = ["zach", "lauren", "logan"]
print(strs)

#Accessing/Traversing the list
shoppingList = ["Milk", "Cheese", "Butter", "Bread"]
print(shoppingList[3]) # Prints Bread

# python allows for list index to be negative
# it will count backwards down the list
print(shoppingList[-1]) # Prints Bread


# boolean operator: can return true or false depend on if milk is in the list
print("Ham" in shoppingList) # Prints True

for i in shoppingList:
    print(i)

for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i]+"+"
    print(shoppingList[i])

# Update/Insert - List
myList = [1,2,3,4,5,6,7]
print(myList)
myList.insert(0,11)
print(myList)

newList = [11,22,33]
myList.extend(newList)
print(myList)
