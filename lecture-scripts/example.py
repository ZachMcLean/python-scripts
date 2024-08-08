def potato():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    gpa = float(input("Enter your gpa: "))

    age = age * 3

    print(f'Hello {name}!', end='')
    print(f'You are a boomer: {age}', end='')
    print(f'Your gpa: {gpa}')
    print()
    print(type(name), type(age), type(gpa))
    print(name, age, gpa, sep=":)")
    print(f'{name}:){age}:){gpa}')

if __name__ == "__main__":
    potato()