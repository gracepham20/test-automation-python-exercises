import random

class Card():
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return print("Value:", self.value, "; Suit:", self.suit)

class Deck():
    def __init__(self):
        self.deck = []
        self.cards()

    def cards(self):
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        for v in values:
            for s in suits:
                card = Card(v, s)
                self.deck.append(card)

    def shuffle(self):
        random.shuffle(self.deck)
        return self.deck

    def deal(self):
        newDeck = self.shuffle()
        return newDeck[0]

deckA = Deck()
deckB = Deck()
print(deckA.deal())
print(deckB.deal())