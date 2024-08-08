def main():
    age = int(input("Enter your age: ")) # cout << "enter your age: " ; cin >> age;
    if age >= 30:
        print("You're a boomer.")
        if age > 59:
            print("You're an ultra boomer boomer")
        else:
            print("Hi")
    elif 18 < age < 30: # if (age < 30 && age > 18)
        print("you're an almost boomer")
    else:
        print("You're a zoomer")



if __name__ == "__main__":
    main()