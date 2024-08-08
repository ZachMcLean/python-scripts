def main():
    start = int(input("Enter start value: "))
    stop = int(input("Enter stop value: "))
    step = int(input("Enter step value: "))

    for i in range(start, stop, step):
        print(f"{i:4d}: Hello World")

    print(f'{i} after the loop')

    stuff = input("Enter some text: ")

    for ch in stuff:
        print(ch)
        if ch == 'l':
            break
    else:
        print("IN THE FOR ELSE")
    print(stuff)
        

    for x in range(1, 10):
        for y in range(1, 10):
            print(f'{x * y:>4d}', end='')
            if y == 4:
                break
        print()



if __name__ == "__main__":
    main()