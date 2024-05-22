
import os
# Lists in python
# theyre just arrays
food = ['pizza', "hamburger", "hotdog", "spaghetti", "pudding"]

print(food[0])

food.append("ice cream")
food.remove("hotdog")
food.pop()
food.insert(0, "cake")
food.sort()
food.clear()

for x in food:
  print(x)


# tuple = collection which is ordered and unchangeable
#         used to group together related data

student = ("Bro", 21, "male")
print(student.count("Bro"))

for i in student:
    print(i)

if "Bro" in student:
    print("Bro is here!")


# sets = a collection which is unordered, unindexed, and allows for no duplicates



# with open(home/zach/.config/zsh/zshenv.txt) as file:

def multiply_numbers(n):
    return n*n

print(multiply_numbers(100))

#     print(file.read())
