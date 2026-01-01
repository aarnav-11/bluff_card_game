import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Player:
    def __init__(self, username, cards=None):
        self.username = username
        self.cards = [] if cards is None else cards

    def addCard(self, card: Card):
        self.cards.append(card)

Aarnav = Player("Aarnav")
Keegan = Player("Keegan")

def dealCards(deck, players, cards_each=5):
    random.shuffle(deck)
    for i in range(cards_each):
        for player in players:
            player.addCard(deck.pop())

deck = [Card(value, suit) for value in ["2","3","4","5","6","7","8","9","10","J","Q","K","A"] for suit in ["hearts","diamonds","clubs","spades"]]

if __name__ == "__main__":
    players = [Aarnav, Keegan]
    dealCards(deck, players, cards_each=5)

    for p in players:
        print(p.username, p.cards)

    print("Cards left in deck:", len(deck))