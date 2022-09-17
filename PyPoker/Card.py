import enum


class Card:
    def __init__(self, suit, order):
        self.suit = suit
        self.order = order

    def __str__(self):
        return f"{self.order.name.capitalize()} of {self.suit.name.capitalize()}"


class PokerCard:
    @staticmethod
    class Order(enum.Enum):
        ACE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
        SIX = 6
        SEVEN = 7
        EIGHT = 8
        NINE = 9
        JACK = 10
        QUEEN = 11
        KING = 12

    @staticmethod
    class Suit(enum.Enum):
        CLUBS = 0
        DIAMONDS = 1
        HEARTS = 2
        SPADES = 3
