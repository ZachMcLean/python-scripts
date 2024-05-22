# num1 = int(input("Please input a number: "))
num, check = input("Please enter a num and a check: ").split()

int(check)
if (int(num) % 2 == 0):
    print("its even")
    if (int(num) % 4 == 0):
        print("its divisible by 4")
else:
    print("its odd")

if(int(num) % int(check) == 0):
    print(check + "is divisible by " + num)
