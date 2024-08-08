import sys
import random 

def main():
    
    outfile = open(sys.argv[1], 'a')

    l  = ['10', '2', 3]

    for e in l:
        print(str(e), file=outfile)

    x = 33
    value = 7.34
    s = 'Robert'
   
    print(s, x, value, sep=', ', file=outfile)
    print()
    
    outfile.close()

 


    # with open(sys.argv[1], 'w') as outfile:
    #     # stuff to do while outfile exists 
          # print(s, x, value, sep=', ', file=outfile)




  


if __name__ == "__main__":
    main()