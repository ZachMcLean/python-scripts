import random


class Card:

    """Represents a playing card."""

    def __init__(self, suit, name, point_value):

        self.suit = suit

        self.name = name

        self.point_value = point_value


    def __add__(self, other):

        """Allows adding two cards or a card and an integer."""

        if isinstance(other, Card):

            return self.point_value + other.point_value

        elif isinstance(other, int):

            return self.point_value + other

        else:

            raise TypeError("Unsupported operand type for +")


    def __radd__(self, other):

        """Allows sum() to be used on an iterable of Cards."""

        return self.__add__(other)


    def __repr__(self):

        return f"{self.name} of {self.suit}"


class Deck:

    """Represents a deck of cards."""

    def __init__(self):

        self.cards = []

        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

        self.names = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]


        for suit in self.suits:

            for name in self.names:

                point_value = self.calculate_point_value(name)

                self.cards.append(Card(suit, name, point_value))


    def calculate_point_value(self, name):

        """Calculates the point value of a card based on its name."""

        if name == "Ace":

            return 1

        elif name in ["Jack", "Queen", "King"]:

            return 10

        else:

            return int(name)


    def shuffle(self):

        """Shuffles the deck."""

        random.shuffle(self.cards)


    def draw(self, num_cards):

        """Draws one or more cards from the deck."""

        if num_cards > len(self.cards):

            raise ValueError("Not enough cards in the deck")

        drawn_cards = self.cards[:num_cards]

        self.cards = self.cards[num_cards:]

        return drawn_cards


    def reset(self):

        """Resets the deck to its original state and shuffles."""

        self.cards = []

        for suit in self.suits:

            for name in self.names:

                point_value = self.calculate_point_value(name)

                self.cards.append(Card(suit, name, point_value))

        self.shuffle()


    def __len__(self):

        return len(self.cards)


    def add_card(self, card, position=None):

        """Adds a card to the deck at a specified position."""

        if position is None:

            self.cards.append(card)

        else:

            self.cards.insert(position, card)


class Hand:

    """Represents a hand of cards."""

    def __init__(self, size=5):

        self.cards = []

        self.size = size


    def add_card(self, card):

        """Adds a card to the hand."""

        if len(self.cards) < self.size:

            self.cards.append(card)

        else:
            print("hand is full")
            # raise ValueError("Hand is full")


    def discard_card(self, card):

        """Discards a card from the hand."""

        self.cards.remove(card)


    def calculate_score(self):

        """Calculates the score of the hand."""

        return sum(self.cards)


    def __len__(self):

        return len(self.cards)


    def __repr__(self):

        return f"Hand of {self.cards}"


def play_blackjack():

    deck = Deck()

    deck.shuffle()


    player_hand = Hand(size=2)

    dealer_hand = Hand(size=2)


    player_hand.add_card(deck.draw(1)[0])

    player_hand.add_card(deck.draw(1)[0])


    dealer_hand.add_card(deck.draw(1)[0])

    dealer_hand.add_card(deck.draw(1)[0])


    print("Your hand:", player_hand)

    print("Dealer's up card:", dealer_hand.cards[0])


    while True:

        action = input("Do you want to hit or stand? ")

        if action.lower() == "hit":

            player_hand.add_card(deck.draw(1)[0])

            print("Your hand:", player_hand)

            if player_hand.calculate_score() > 21:

                print("You busted! Dealer wins.")

                return

        elif action.lower() == "stand":

            break

        else:

            print("Invalid input. Please enter 'hit' or 'stand'.")


    while dealer_hand.calculate_score() < 17:

        dealer_hand.add_card(deck.draw(1)[0])


    print("Dealer's hand:", dealer_hand)


    if dealer_hand.calculate_score() > 21:

        print("Dealer busted! You win.")

    elif dealer_hand.calculate_score() < player_hand.calculate_score():

        print("Your score is higher. You win.")

    elif dealer_hand.calculate_score() > player_hand.calculate_score():

        print("Dealer's score is higher. Dealer wins.")

    else:

        print("It's a tie!")


play_blackjack()
