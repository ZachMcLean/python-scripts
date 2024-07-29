from Hand import Hand
from Deck import Deck

def main():
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


if __name__ == "__main__":
    main()
