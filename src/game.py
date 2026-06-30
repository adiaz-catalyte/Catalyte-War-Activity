"""
    Main game logic.
    Responsibilities:
        initializing the players and game
        deal cards
        play rounds
        resolve wars
        determine the winner
        print the game status
"""
from src.deck import Deck
from src.player import Player

class Game:
    def __init__(self, player1_name, player2_name):
        """
        Initializes the game with two players and a deck of cards.

        Parameters:
            player1_name (str): The name of the first player.
            player2_name (str): The name of the second player.
        """
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.deck = Deck()
        self.deal_cards()