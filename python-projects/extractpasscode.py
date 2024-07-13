def main():
    print('---CID Passcode Extractor---')
    passcode = ''
    previous_value_str = ''
    recent_pair = False

    while True:
        line = input('Enter line: ')
        if line == 'end':
            break

        first_digit = None
        last_digit = None

        for char in line:
            if '0' <= char <= '9':  # Checking if the character is a digit
                if first_digit is None:
                    first_digit = char
                last_digit = char

        if first_digit is None: # if no digits in message, subtract 1 from previous digit pair
            print('-1 extracted')
            if recent_pair:
                previous_value = int(previous_value_str) - 1
                previous_value_str = str(previous_value)
                passcode = passcode[:-len(previous_value_str)] + previous_value_str
                recent_pair = True
        else:
            if last_digit is None:
                last_digit = first_digit
            extracted_value = int(last_digit + first_digit)
            print(f'{extracted_value} extracted')
            passcode += str(extracted_value)
            previous_value_str = str(extracted_value)
            recent_pair = True

    if passcode:
        print(f'The passcode is: {passcode}')
    else:
        print('No passcode was extracted.')

if __name__ == "__main__":
    main()
