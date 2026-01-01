
import random

playerList = []
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

print(playerList)

class Player:
    def __init__ (self, username, cards = []):
        self.username = username
        self.cards = cards
        playerList.append(self)

    def addCard(self, card: Card):
        self.cards.append(card)

Aarnav = Player("Aarnav")
print(Aarnav.cards)

def dealCards(deck, player):
    pass

deck = [Card(value, suit) for value in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] for suit in ["hearts", "diamonds", "clubs", "spades"]]
random.shuffle(deck)


# for card in deck:
#     print(card.value, "of", card.suit)