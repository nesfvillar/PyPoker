from Card import *


class PokerDeck:
    cards = [Card(suit, order) for suit in PokerCard.Suit for order in PokerCard.Order]

    def __init__(self):
        self._remaining_cards = set(PokerDeck.cards)

    def pull_card(self):
        if len(self._remaining_cards) > 0:
            return self._remaining_cards.pop()

    def shuffle(self):
        self._remaining_cards.update(PokerDeck.cards)
