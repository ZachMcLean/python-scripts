import random
import sys

def main():
    filename =''
    if len(sys.argv) > 5:
        return
    for i, elem in enumerate(sys.argv):
        if i in [0, 1]:
            continue
        try:
            sys.argv[i] = int(elem)
        except ValueError:
             print(f'{sys.argv[i]} is not an integer...try again')
             return

    match len(sys.argv):
        case 2:
            generate_file(sys.argv[1])
        case 3:
            generate_file(sys.argv[1], sys.argv[2])
        case 4:
            generate_file(sys.argv[1], sys.argv[2], sys.argv[3])
        case 5:
            generate_file(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
        case _:
            print("USAGE: python file_gen.py filename [num_bets] [choice_size] [pool_size]")
            return


def generate_file(filename, num_bets=5, choice_size=5, pool_size=8):
    with open(filename, 'w') as outfile:
        for i in range(num_bets):
            print(f"Bet {i+1: {len(str(num_bets)) + 1}d}:", end='', file=outfile)
            choices = generating_set(choice_size)
            for choice in choices:
                print(f'{choice:3d}', end='', file=outfile)
            print(" =>", end='', file=outfile)
            pool = generating_set(pool_size)
            for p in pool:
                print(f'{p:3d}', end='', file=outfile)
            print(file=outfile)

def generating_set(size):
    if size < 0:
        size = random.randint(5, 25)
    my_set = set()
    while len(my_set) < size:
        my_set.add(random.randint(1, 99))
    return my_set

if __name__ == "__main__":
    main()