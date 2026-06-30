"""
    Represents a player in the game.
    Responsibilities:
        player's pile of cards
        drawing a card
        collection of won cards
        determining if player has cards left
"""

class Player:
    def __init__(self, name):
        """
        Initializes a new player with a name and an empty pile of cards.

        Parameters:
            name (str): The name of the player.
        """
        self.name = name
        self.pile = []

    def draw_card(self):
        """
        Draws a card from the player's pile.

        Returns:
            Card: The card drawn from the player's pile.
            None: If the player's pile is empty.
        """
        if self.has_cards():
            return self.pile.pop(0)
        else:
            return None

    def add_cards(self, cards):
        """
        Adds won cards to the player's pile.

        Args:
            cards (list): A list of Card objects to be added to the player's pile.
        """
        self.pile.extend(cards)

    def has_cards(self):
        """
        Checks if the player has any cards left in their pile.

        Returns:
            bool: True if the player has cards left, False otherwise.
        """
        return len(self.pile) > 0