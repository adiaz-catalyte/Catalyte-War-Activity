"""
    Responsible only for the deck.
    class will:
        create all 52 cards
        shuffle the deck
        deal the cards
        know if deck is empty
"""
from card import Card
import random

class Deck:
    def __init__(self):

        '''
        Initializes a new deck of cards and shuffles it.
        '''
        self.cards = self.create_deck()
        self.shuffle_deck()

    def create_deck(self):

        """
        Creates a standard deck of 52 cards.
        Returns:
            list: A list containing 52 Card objects.
        """
        return [Card(rank, suit) for suit in Card.SUITS for rank in Card.VALUE_TABLE.keys()]

    def shuffle_deck(self):
        """
        Shuffles the deck of cards in place.
        """
        random.shuffle(self.cards)

    def deal_cards(self):

        """
        Deals the cards evenly between two players.
        Returns:
            tuple: A tuple containing two lists of Card objects.
        """
        mid = len(self.cards) // 2
        return self.cards[:mid], self.cards[mid:]

    def draw_card(self):

        """
        Draws a card from the top of the deck.
        Returns:
            Card: The card drawn from the deck.
        Raises:
            ValueError: If the deck is empty.
        """
        if not self.is_empty():
            return self.cards.pop(0)
        else:
            raise ValueError("The deck is empty. Cannot draw a card.")

    def is_empty(self):
        
        """
        Checks if the deck is empty.
        Returns:
            bool: True if the deck is empty, False otherwise.
        """
        return len(self.cards) == 0