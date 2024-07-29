from Card import Card
import random

class Deck:
    # Represents a deck of cards.
    def __init__(self):
        # self.cards - []
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.names = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        
        for suit in self.suits:
            for name in self.names:
                point_value = self.calculate_point_value(name)
                self.cards.append(Card(suit, name, point_value))

        # Calculates the point value of a card based on its name.
    def calculate_point_value(self, name):
        if name == "Ace":
            return 1

        elif name in ["Jack", "Queen", "King"]:
            return 10

        else:
            return int(name)

    def shuffle(self):

        # Shuffles the deck.
        random.shuffle(self.cards)

    def draw(self, num_cards):

        # Draws one or more cards from the deck.
        if num_cards > len(self.cards):
            raise ValueError("Not enough cards in the deck")

        drawn_cards = self.cards[:num_cards]
        self.cards = self.cards[num_cards:]
        return drawn_cards

    def reset(self):

        # Resets the deck to its original state and shuffles.
        self.cards = []

        for suit in self.suits:
            for name in self.names:
                point_value = self.calculate_point_value(name)
                self.cards.append(Card(suit, name, point_value))

        self.shuffle()

    def __len__(self):
        return len(self.cards)

    def add_card(self, card, position=None):

        # Adds a card to the deck at a specified position.
        if position is None:
            self.cards.append(card)

        else:
            self.cards.insert(position, card)

