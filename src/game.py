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
from card import Card
from deck import Deck
from player import Player

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
        self.round_number = 0

    def deal_cards(self):
        """
        Deals the cards from the deck to both players.
        """
        player1_hand, player2_hand = self.deck.deal_cards()
        self.player1.add_cards(player1_hand)
        self.player2.add_cards(player2_hand)

    def higher_card_winner(self, player1: Player, player1_card: Card, player2: Player, player2_card: Card):
        """
        Compairs each players card and returns the player with the greater card
        and None if the cards are of equal value.

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
        Player, Card
            If the cards are not equal then the player with the higher card is returned
            and the higher Card is also returned
        None
            If the cards of both players is equal then None is returned
        """
        if player1_card == player2_card:
            return None, None
        if player1_card.get_card_value() > player2_card.get_card_value():
            return player1, player1_card
        else:
            return player2, player2_card
    
    def play_round(self):
        """
        Plays a single round of the game.
        Each player draws a card, and the player with the higher card wins the round.
        In case of a tie, a war is initiated.

        Returns:
            str: The result of the round.
        """
        if self.player1.has_cards() and self.player2.has_cards():
            card1 = self.player1.draw_card()
            card2 = self.player2.draw_card()

            player_round_winner, winning_card = self.higher_card_winner(self.player1, card1, self.player2, card2)
            if player_round_winner == None:
                return self.resolve_war([card1], [card2])
            else:
                player_round_winner.add_cards([card1, card2])
                return f"{player_round_winner.name} wins the round!"
        else:
            return "Game over. One of the players has no cards left."

    def resolve_war(self, war_pile1, war_pile2):
        """
        Resolves a war situation when both players draw cards of equal value.
        Each player places three cards face down and one card face up.
        The player with the higher face-up card wins all the cards in the war pile.

        Args:
            war_pile1 (list): The pile of cards from player 1 involved in the war.
            war_pile2 (list): The pile of cards from player 2 involved in the war.

        Returns:
            str: The result of the war.
        """
        if len(self.player1.pile) < 4 or len(self.player2.pile) < 4:
            return "Game over. One of the players does not have enough cards for war."

        # Each player places three cards face down and one card face up
        for _ in range(3):
            war_pile1.append(self.player1.draw_card())
            war_pile2.append(self.player2.draw_card())

        card1 = self.player1.draw_card()
        card2 = self.player2.draw_card()
        war_pile1.append(card1)
        war_pile2.append(card2)

        if card1.value > card2.value:
            self.player1.add_cards(war_pile1 + war_pile2)
            return f"{self.player1.name} wins the war!"
        elif card2.value > card1.value:
            self.player2.add_cards(war_pile1 + war_pile2)
            return f"{self.player2.name} wins the war!"
        else:
            return self.resolve_war(war_pile1, war_pile2)  # Recursive call for another tie
        
    def determine_winner(self):
        """
        Determines the winner of the game based on the number of cards each player has.

        Returns:
            str: The name of the winning player or a message indicating a tie.
        """
        if len(self.player1.pile) > len(self.player2.pile):
            return f"{self.player1.name} wins the game!"
        elif len(self.player2.pile) > len(self.player1.pile):
            return f"{self.player2.name} wins the game!"
        else:
            return "The game is a tie!"
        
    def print_game_status(self):
        """
        Prints the current status of the game, including the number of cards each player has.
        """
        print(f"{self.player1.name} has {len(self.player1.pile)} cards.")
        print(f"{self.player2.name} has {len(self.player2.pile)} cards.")

    def _pause_for_next_round(self):
        input("Press Enter to continue to the next round...")
