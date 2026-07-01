"""
    Starts the game.
"""
from game import Game

def main():
    """
    Main function to start the game.
    Initializes the game with two players and plays rounds until one player runs out of cards.
    """
    print("Welcome to the War Card Game!")
    player1_name = input("Enter the name of Player 1: ")
    player2_name = input("Enter the name of Player 2: ")
    print("\nStarting the game...\n")
    game = Game(player1_name, player2_name)

    while game.player1.has_cards() and game.player2.has_cards():
        result = game.play_round()
        print(result)
        game.pause_for_next_round()
    if not game.player1.has_cards():
        print(f"{game.player2.name} wins the game!")
    else:
        print(f"{game.player1.name} wins the game!")

if __name__ == "__main__":
    main()
