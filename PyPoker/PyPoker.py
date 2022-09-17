from Deck import *
from Hand import *


def main():
    deck = PokerDeck()
    hand_a = PokerHand()
    hand_b = PokerHand()
    for _ in range(5):
        hand_a.add_card(deck.pull_card())
        hand_b.add_card(deck.pull_card())

    print(hand_a, hand_b, sep='\n')


if __name__ == "__main__":
    main()
