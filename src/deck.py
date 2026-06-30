import random

class Deck:
    """Represents a standard deck of 52 playing cards."""
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    
    def __init__(self):
        self.cards = [(suit, value) for suit in self.suits for value in self.values]

    def from_tuple(self, cards: list[tuple[str, str]]):
        self.cards = [(suit, value) for suit in cards[0] for value in cards[1]]

    def __len__(self):
        return len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)
        return self

    def deal_cards(self):
        half_deck = len(self.cards) // 2
        player1_hand = self.from_tuple(self.cards[:half_deck])
        player2_hand = self.from_tuple(self.cards[half_deck:])
        return player1_hand, player2_hand
    
    def draw_card(self):
        if self.cards:
            return self.cards.pop(0)
        else:
            return None

    def reset(self):
        self.cards = [(suit, value) for suit in self.suits for value in self.values]
        return self
