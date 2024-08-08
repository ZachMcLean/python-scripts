# access to variables used or maintained by the interpreter 
# and to functions that interact strongly with the interpreter
import sys 
# sys.argv -> List of command line args passed to script
# argv[0] is script name, or '-c', or '' depending on how the
#   interpreter was executed


def main():
    print(sys.argv)
    for i, item in enumerate(sys.argv):
        print(f'{i:2d}: {type(item)} - {item}')


if __name__ == "__main__":
    main()