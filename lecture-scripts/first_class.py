
import gc

class Date:
    def __init__(self, m=1, d=1, y=1900):
        self.month = m
        self.day = d
        self.year = y

    def __del__(self):
        print("Deleting", self.__repr__())

    def __str__(self):
        return f'{self.month}/{self.day}/{self.year}'

    def __repr__(self):
        return f'Date({self.month}, {self.day}, {self.year})'



def main():
    today = Date(7, 22, 2024)
    print(today)
    tomorrow = Date()
    print(tomorrow)
    another = Date(3)
    print(another)
    other = Date(y=17)
    print(other)
    
    

    other.child = today
    today.child = other


if __name__ == "__main__":
    main()

