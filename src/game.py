# game logic for War Card Game
# Requirments:
# 1. The game needs a deck of 52 playing cards
# 2. The cards should be of 4 suits, Hearts, Spades, Clubs and Diamonds, and each suit will
# have cards with the values of A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, and K, where A is the lowest
# and K is the highest .
# 3. The deck of cards will need to be shuffled before being dealt.
# 4. For the deal, the cards will be divided evenly, with each player receiving 26 cards, face
# down.
# 5. The winner is the player with the most cards after all the cards have been played.
# 6. The output of each card flip should be printed to the console.
# Console output should look similar to the following:
# Round 0 of War
# Player 1: 2 of Spades
# Player 2: 3 of Spades
# Player 2 Wins The War

# Stretch Requirements:
# 1. The winner of each round shuffles the cards won that round and adds them to the bottom
# of their current deck (this prevents flip-flopping games). The game ends when one player
# wins all 52 cards.
# 2. If wars continue to happen until one player runs out of cards, the player with the most
# cards wins.

try:
    from deck_of_cards import Deck
except ImportError:  # pragma: no cover - fallback for package-style execution
    from .deck_of_cards import Deck


class Game:
    """Represents a game of War between two players."""

    def __init__(self, deck=None):
        self.deck = Deck() if deck is None else deck
        self.deck = self.deck.shuffle()
        self.player1_hand, self.player2_hand = self.deck.deal_cards()
        self.round_number = 0
        self.cards_played = 0

    def play_round(self):
        if not self.player1_hand or not self.player2_hand or self.cards_played >= 52:
            return False

        self.round_number += 1
        print(f"Round {self.round_number} of War")

        player1_card = self.player1_hand.pop(0)
        player2_card = self.player2_hand.pop(0)
        self.cards_played += 1

        print(f"Player 1: {player1_card[1]} of {player1_card[0]}")
        print(f"Player 2: {player2_card[1]} of {player2_card[0]}")

        player1_value = self.card_value(player1_card)
        player2_value = self.card_value(player2_card)

        if player1_value > player2_value:
            print("Player 1 Wins The War")
            self.player1_hand.extend([player1_card, player2_card])
        elif player2_value > player1_value:
            print("Player 2 Wins The War")
            self.player2_hand.extend([player1_card, player2_card])
        else:
            print(f"IT\'S A WAR...YOU BOTH DREW A {player1_card[1]} OF {player1_card[0]}") # implement war functionality
            self.commit_war()
        print()
        if self.player1_hand and self.player2_hand:
            self._pause_for_next_round()
        return True

    def play_game(self):
        print("Starting a new game of War!")

        while self.player1_hand and self.player2_hand and self.cards_played < 52:
            self.play_round()

        self._print_final_results()

    def _pause_for_next_round(self):
        input("Press Enter to continue to the next round...")

    def commit_war(self):
        player_1_cards_down = []
        player_2_cards_down = []

        for i in range(0,4):
            self.player1_hand
            

    def _print_final_results(self):
        print("Game Over!")
        print(f"Player 1 cards: {len(self.player1_hand)}")
        print(f"Player 2 cards: {len(self.player2_hand)}")

        if len(self.player1_hand) > len(self.player2_hand):
            print("Player 1 Wins The Game!")
        elif len(self.player2_hand) > len(self.player1_hand):
            print("Player 2 Wins The Game!")
        else:
            print("It's a tie!")

    @staticmethod
    def card_value(card):
        """Returns the value of the card for comparison."""
        value_order = {
            "A": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "J": 11,
            "Q": 12,
            "K": 13,
        }
        return value_order[card[1]]