import shapes

pi = 3.14

def main():
    one = shapes.Rectangle(5, 4)
    print(one)
    two = shapes.Rectangle(5, 4)
    print(two)
    print(len(one))

    if one:
        print("It's TRUE")
    else:
        print("It's FALSE")

    if one != 5:
        print("NOT EQUAL")
    else:
        print("EQUAL")

    if one is two:
        print("They are the same identity")
    else:
        print(id(one), id(two))

    print(int(one))
    # three = two + one
    # print(three)
    # one = one + 3.14
    # print(one)
    # one = 3 + one
    # print(one)
    # one += 3
    # print(one)
    





if __name__ == "__main__":
    main()