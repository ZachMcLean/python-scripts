# Zach McLean
# CSCI 3038?
# Nebula Numbers

# Read a file line by line into a list (or maybe 2 lists?),
# loop over that list and compare to the other list
# for every match inside the list, 
#  if it is the first match, add 1
#  else, double it

# reset the counter for each bet round, total up all tokens at the end

import sys
import os

def calculate_tokens(bet_line):
    parts = bet_line.split("=>")
    
    # Extract the bettor's numbers
    bet_numbers = parts[0].split()
    bet_numbers = bet_numbers[1:]  # Ignore the first part (e.g., "Bet 1:")
    bet_numbers = [int(num) for num in bet_numbers]
    
    # Extract the draw pool numbers
    draw_pool = parts[1].split()
    draw_pool = [int(num) for num in draw_pool]
    
    matched_numbers = []
    for num in bet_numbers:
        if num in draw_pool:
            matched_numbers.append(num)
            draw_pool.remove(num)  # Remove to handle duplicates

    return matched_numbers

def process_bets(file_path):
    total_tokens = 0
    matches = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip():  # Check if the line is not empty
                    matched_numbers = calculate_tokens(line.strip())
                    matches.append(matched_numbers)
                    total_tokens += len(matched_numbers)
    except FileNotFoundError:
        print(f"ERROR: {file_path} could not be opened...")
        return None, None
    
    return matches, total_tokens

def main():
    if len(sys.argv) != 2:
        print("ERROR: missing arguments for correct usage")
        print("USAGE: python nebulanumbers.py filename")
        return
    
    file_path = sys.argv[1]
    matches, total_tokens = process_bets(file_path)
    
    if matches is not None and total_tokens is not None:
        print("------Matches------")
        for i, match in enumerate(matches, 1):
            if match:
                print(f"{i}: {match}")
            else:
                print(f"{i}: None")
        print(f"Tokens Won: {total_tokens}")
    
if __name__ == "__main__":
    main()
