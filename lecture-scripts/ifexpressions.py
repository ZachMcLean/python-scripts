def main():
    age = int(input("Enter your age: ")) # cout << "enter your age: " ; cin >> age;

    print(f"{'adult' if age > 21 else 'child'   }")

    text = input("Enter text: ")
    if text < 0 and text > 'a':
        print("lowercase")
    else:
        print("not")

if __name__ == "__main__":
    main()