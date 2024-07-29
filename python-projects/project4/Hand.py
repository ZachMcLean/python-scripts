class Hand:

    # Represents a hand of cards.
    def __init__(self, size=5):
        self.cards = []
        self.size = size

    def add_card(self, card):

        # Adds a card to the hand.

        if len(self.cards) < self.size:
            self.cards.append(card)

        else:
            raise ValueError("Hand is full")


    def discard_card(self, card):

        # Discards a card from the hand.
        self.cards.remove(card)

    def calculate_score(self):

        # Calculates the score of the hand.
        return sum(self.cards)

    def __len__(self):
        return len(self.cards)

    def __repr__(self):
        return f"Hand of {self.cards}"
