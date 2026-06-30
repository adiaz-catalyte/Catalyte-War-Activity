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
from src.card import Card
from src.deck import Deck
from src.player import Player

class Game:
    def __init__(self, player1_name, player2_name):
        """
        Initializes the game with two players and a deck of cards.

        Args:
            player1_name (str): The name of the first player.
            player2_name (str): The name of the second player.
        """
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.deck = Deck()
        self.deal_cards()

    def higher_card_winner(self, player1: Player, player1_card: Card, player2: Player, player2_card: Card):
        """
        Compairs each players card and returns the player with the greater card
        and None if the cards are of equal value

        Parameters
        ----------
        player1 : Player
            The player who has the player1_card
        player1_card : Card
            The card played by the Player from the player1 argument
        player2 : Player
            The player who has the player2_card
        player2_card : Card
            The card played by the Player from the player2 argument

        Returns
        -------
        Player
            If the cards are not equal then the player with the higher card is returned
        None
            If the cards of both players is equal then None is returned
        """
        if player1_card == player2_card:
            return None
        if player1_card.get_card_value() > player2_card.get_card_value():
            return player1
        else:
            return player2