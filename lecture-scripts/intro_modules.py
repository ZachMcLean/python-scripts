import random
import more_classes
from shapesv2 import Dog

def main():
    print(random.randint(1, 100))
    print(more_classes.pi)
    one()
    d = Dog("billy")
    d.bark()

def one():
    pi = 7.78
    def two():
        print(pi)

    two()


if __name__ == "__main__":
    main()
    
    

