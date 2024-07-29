class Card:

    # Represents a playing Card
    def __init__(self, suit, name, point_value):
        self.suit = suit
        self.name = name
        self.point_value = point_value

    def __add__(self, other):

        #Allows adding two cards or a card and an integer.
        if isinstance(other, Card):
            return self.point_value + other.point_value

        elif isinstance(other, int):
            return self.point_value + other

        else:
            raise TypeError("Unsupported operand type for +")

    def __radd__(self, other):

        # Allows sum() to be used on an iterable of Cards.
        return self.__add__(other)

    def __repr__(self):

        return f"{self.name} of {self.suit}"
