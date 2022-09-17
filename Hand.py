from Card import *


class Hand:
    def __init__(self):
        self.hand = []

    # TODO figure out what to do if card is None (deck is empty)
    def add_card(self, card):
        self.hand.append(card)

    def clear(self):
        self.hand.clear()

    def size(self):
        return len(self.hand)

    def ranking(self):
        raise NotImplementedError

    def __lt__(self, other):
        raise NotImplementedError

    def __ne__(self, other):
        raise NotImplementedError

    def __str__(self):
        return str([str(card) for card in self.hand])


class PokerHand(Hand):
    @staticmethod
    class Rankings(enum.Enum):
        STRAIGHT_FLUSH = 0
        FOUR_OF_A_KIND = 1
        FULL_HOUSE = 2
        FLUSH = 3
        STRAIGHT = 4
        THREE_OF_A_KIND = 5
        TWO_PAIR = 6
        ONE_PAIR = 7
        HIGH_CARD = 8

    # TODO parse hand into Ranking enum
    def ranking(self):
        if self.size() == 5:
            pass

    # TODO check situations where one hand loses to the other
    def __lt__(self, other):
        if self.ranking() < other.ranking():
            return True
        else:
            pass

    # TODO check situations where the hands are not equal
    def __ne__(self, other):
        pass
