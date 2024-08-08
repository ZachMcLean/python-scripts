
class Rectangle:
    def __init__(self, length=0, width=0):
        self.length = length
        self.width = width
    
    def __str__(self):
        return f'{self.length}, {self.width}'

    def __add__(self, other):
        match other:
            case Rectangle():
                return Rectangle(self.length + other.length, self.width + other.width)
            case int() | float():
                return Rectangle(self.length + other, self.width + other)
            case _:
                return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other): # +=
        return self.__add__(other)

    def __bool__(self):
        if self.length <= 0 or self.width <= 0:
            return False
        return True
    
    def __len__(self):
        return self.width * 2 + self.length * 2
    
    def __eq__(self, other):
        match other:
            case Rectangle():
                return self.length == other.length and self.width == other.width
            case int() | float():
                return self.length == other and self.width == other
            case _:
                return NotImplemented

    def __int__(self):
        return self.width * self.length


class Circle:
    pass


if __name__ == "__main__":
    r = Rectangle(2,3)
    print(r)