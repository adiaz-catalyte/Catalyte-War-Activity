from src.player import Player

def test_player_initialization():
    player = Player("Alice")
    assert player.name == "Alice"
    assert player.pile == []

def test_draw_card():
    player = Player("Bob")
    card1 = "Card1"
    card2 = "Card2"
    player.add_cards([card1, card2])
    
    drawn_card = player.draw_card()
    assert drawn_card == card1
    assert player.pile == [card2]

def test_add_cards():
    player = Player("Charlie")
    cards_to_add = ["Card1", "Card2"]
    player.add_cards(cards_to_add)
    
    assert player.pile == cards_to_add

def test_has_cards():
    player = Player("Diana")
    assert not player.has_cards()  # Initially, the player has no cards
    
    player.add_cards(["Card1"])
    assert player.has_cards()  # Now the player has cards