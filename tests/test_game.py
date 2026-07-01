from src.game import Game

def test_game_initialization():
    game = Game("Alice", "Bob")
    assert game.player1.name == "Alice"
    assert game.player2.name == "Bob"
    assert len(game.player1.pile) == 26  # Each player should have half the deck
    assert len(game.player2.pile) == 26

