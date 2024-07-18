# Zach McLean
# CSCI 3038
# Nebula Numbers

# Read a file line by line into a list (or maybe 2 lists?),
# loop over that list and compare to the other list
# for every match inside the list, 
#  if it is the first match, add 1
#  else, double it

#    Process the bets in the file and return a dictionary of matches and the total tokens won.

import sys

def process_bets(file_name):
    try:
        # Open the file and initialize the matches dictionary and total tokens
        with open(file_name, 'r') as file:
            matches = {}
            total_tokens = 0

            for i, line in enumerate(file, start=1):
                # Split the line into the bet and the drawn pool
                bet, drawn_pool = line.strip().split(' => ')

                # Extract the chosen numbers from the bet
                _, *chosen_numbers = bet.split()
                chosen_numbers = set(map(int, [num.strip(':') for num in chosen_numbers]))

                # Extract the drawn numbers from the drawn pool
                drawn_numbers = set(map(int, drawn_pool.split()))

                # Calculate the match
                match = chosen_numbers & drawn_numbers

                if match:
                    # If there's a match, add it to the matches dictionary and increment the total tokens
                    matches[i] = list(match)
                    total_tokens += len(match)

                else:
                    # If there's no match, add None to the matches dictionary
                    matches[i] = None

            return matches, total_tokens

    except FileNotFoundError:
        # If the file cannot be opened, print an error message and return None
        print(f"ERROR: {file_name} could not be opened...")
        return None, None


if __name__ == "__main__":
    # Check if the command line argument is provided
    if len(sys.argv)!= 2:
        print("ERROR: missing arguments for correct usage")
        print("USAGE: python nebulanumbers.py filename")

    else:
        # Get the file name from the command line argument
        file_name = sys.argv[1]
        # Process the bets and get the matches and total tokens
        matches, total_tokens = process_bets(file_name)

        if matches is not None:
            # Print the matches and total tokens
            print("------Matches------")
            for i, match in matches.items():
                if match is not None:
                    print(f"{i}: {match}")
                else:
                    print(f"{i}: None")

            print(f"Tokens Won: {total_tokens}")
