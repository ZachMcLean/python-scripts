import sys 

def main():
    filename = sys.argv[1]

    try:
        infile = open(filename, 'r' )
    except FileNotFoundError:
        print(f"ERROR: {filename} could not be opened...")
        return




    # for name in infile:
    #     name = name.strip()
    #     quantity = int(infile.readline())
    #     price = float(infile.readline())
    #     print(f"{name}: {quantity}-{price}")
        


    # name = infile.readline() # priming read
    # while name != '': # test if end of file because readline returns '' at EOF
    #     quantity = int(infile.readline())
    #     price = float(infile.readline())
    #     # process that line
    #     name = name.strip()
    #     # do stuff with that line
    #     print(f"{name}: {quantity}-{price}")

    #     name = infile.readline() #recurring read (read the next line)


    # lines = [line.strip() for line in infile ] # alternative to loop below
    
    # infile = open(filename, 'r' )
    # lines = infile.readlines()
    # for i, e in enumerate(lines):
    #     lines[i] = e.strip()
    # print(lines)
    # infile.close()
  
    
    with open(filename ) as infile:
        lines = infile.readlines()
        for i, e in enumerate(lines):
            lines[i] = e.strip()
        print(lines)


if __name__ == "__main__":
    main()