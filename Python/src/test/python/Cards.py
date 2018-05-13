'''
Alec McDaugale
This is a deck of cards. Begining to create a blackJack class. Displays two cards and the value.
'''
import random


class BlackJack:
    def __init__(self):
        self._deck = Deck()
        self._dealer = Player()
        self._player = Player()

    def get_card(self, user):
        index = random.randint(0, 51)
        user.set_index(index)
        user.set_cards(self._deck.get_card(index))

    def deal_cards(self, num):
        for index in range(num):
            self.get_card(self._dealer)
            self.get_card(self._player)

    def get_player_cards(self):
        return self._player

    def get_dealer_cards(self):
        return self._dealer

    def get_total(self, user):
        total = 0
        for index in range(len(user.get_cards())):
            total += user.get_card(index).get_value()
        return total

    def to_string(self):
        print("Dealer")
        print("Total:", self.get_total(self._dealer))
        for index in range(len(self._dealer.get_cards())):
            print(self._dealer.get_card(index).get_card_face(), end=" ")
        print("\n")
        for index in range(len(self._player.get_cards())):
            print(self._player.get_card(index).get_card_face(), end=" ")
        print("\nTotal:", self.get_total(self._player))
        print("Player")


class Player:
    def __init__(self):
        self._cards = []
        self._index = []

    def set_cards(self, card):
        self._cards.append(card)

    def get_cards(self):
        return self._cards

    def get_card(self, index):
        return self._cards[index]

    def set_index(self, index):
        self._index.append(index)

    def get_index(self):
        return self._index


class Deck:
    def __init__(self):
        self._values = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10)
        self._cards = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
        self._suits = ("Hearts", "Diamonds", "Spades", "Clubs")
        self._deck = []
        for suit in self._suits:
            for index in range(len(self._cards)):
                self._deck.append(Card(suit, self._cards[index], self._values[index]))

    def get_deck(self):
        return self._deck

    def get_card(self, index):
        return self._deck[index]

    def to_string(self):
        for index in range(len(self._deck)):
            print(index, end=" ")
            self._deck[index].to_string()


class Card:
    def __init__(self, suit, card, value):
        self._value = value
        self._card = card
        self._suit = suit

    def get_value(self):
        return self._value

    def get_card_face(self):
        return self._card

    def get_suit(self):
        return self._suit

    def to_string(self):
        print(self.get_suit(), self.get_card_face(), self.get_value())


#deck = Deck()
#deck.to_string()
game = BlackJack()
game.deal_cards(2)

game.to_string()

