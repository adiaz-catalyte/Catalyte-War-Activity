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

            print(f"Player {self.player1.name}: {str(card1)}")
            print(f"Player {self.player2.name}: {str(card2)}")

            player_round_winner, winning_card = self.higher_card_winner(self.player1, card1, self.player2, card2)
            if player_round_winner == None:
                return self.resolve_war([], [], [card1, card2])
            else:
                player_round_winner.add_cards([card1, card2])
                return f"{player_round_winner.name} wins the round!"
        else:
            return "Game over. One of the players has no cards left."

    def resolve_war(self, war_pile1, war_pile2, win_pile, round_number=0):
        """
        Resolves a war situation when both players draw cards of equal value.
        Each player places three cards face down and one card face up.
        The player with the higher face-up card wins all the cards in the war pile.
        The war continues if the face-up cards are also of equal value.
        In case a player does not have enough cards to continue the war, the other player wins all the cards.
        If all 4 cards have been tied, the players draw another card to continue the war.

        Args:
            war_pile1 (list): The pile of cards from player 1 involved in the war.
            war_pile2 (list): The pile of cards from player 2 involved in the war.
            win_pile (list): The pile of cards that have been won in the war so far.
            round_number (int): The current round number of the war.

        Returns:
            str: The result of the war.
        """
        if len(self.player1.pile) < 4 or len(self.player2.pile) < 4:
            player_lost, player_won = (self.player1, self.player2) if len(self.player1.pile) < 4 else (self.player2, self.player1)
            player_won.add_cards(win_pile + player_lost.pile)
            player_lost.pile.clear()
            return "Game over. One of the players does not have enough cards for war."

        if (round_number > 0) and ((len(self.player1.pile) == 0) or (len(self.player2.pile) == 0)):
            player_lost, player_won = (self.player1, self.player2) if len(self.player1.pile) == 0 else (self.player2, self.player1)
            player_won.add_cards(win_pile + player_lost.pile)
            player_lost.pile.clear()
            return "Game over. One of the players does not have enough cards for war."


        # Each player places three cards face down and one card face up
        print(f"War! {self.player1.name} and {self.player2.name} draw three cards face down and one card face up.")
        if round_number == 0 and (len(war_pile1) == 0 and len(war_pile2) == 0):
            for _ in range(4):
                war_pile1.append(self.player1.draw_card())
                war_pile2.append(self.player2.draw_card())

        # If all 4 cards have been tied draw another card
        if round_number > 0 and (len(war_pile1) == 0 and len(war_pile2) == 0):
            war_pile1.append(self.player1.draw_card())
            war_pile2.append(self.player2.draw_card())

        card1 = war_pile1.pop()  # The last card drawn is the face-up card for player 1
        card2 = war_pile2.pop()

        print(f"Round {round_number} of The War")
        print(f"Player {self.player1.name}: {str(card1)}")
        print(f"Player {self.player2.name}: {str(card2)}")

        winner, winning_card = self.higher_card_winner(self.player1, card1, self.player2, card2)

        print(f"Player {winner.name if winner else 'None'} Wins The War")

        if winner is None:
            print("The War Continues!")
            return self.resolve_war(war_pile1, war_pile2, win_pile + [card1, card2], round_number=round_number+1)  # Recursive call for another tie
        winner.add_cards(war_pile1 + war_pile2 + [card1, card2] + win_pile)
        return f"{winner.name} wins the war!"
            
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
