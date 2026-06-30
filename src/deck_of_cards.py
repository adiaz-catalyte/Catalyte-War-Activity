import random

class Deck:
    """Represents a standard deck of 52 playing cards."""

    def __init__(self):
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [(suit, value) for suit in self.suits for value in self.values]

    def __len__(self):
        return len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)
        return self

    def deal_cards(self):
        half_deck = len(self.cards) // 2
        player1_hand = self.cards[:half_deck]
        player2_hand = self.cards[half_deck:]
        return player1_hand, player2_hand

    def reset(self):
        self.cards = [(suit, value) for suit in self.suits for value in self.values]
        return self
