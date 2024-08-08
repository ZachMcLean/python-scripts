def main():
    value = int(input("Enter a value: "))
    value2 = input("Enter a name: ")


    match (value, value2):
        case (1, 'Robert'):
            print("one 'Robert' was typed")
        case (1, _):
            print(f"one and {value2} was typed")
        case _:
            print(f'{value} and {value2} was typed')



if __name__ == "__main__":
    main()