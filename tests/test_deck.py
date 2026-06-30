from src.deck_of_cards import Deck

def test_Deck():
    deck = Deck()
    assert len(deck.cards) == 52
    assert isinstance(deck.cards[0], tuple)
    assert isinstance(deck.cards[0][0], str)
    assert isinstance(deck.cards[0][1], str)

def test_shuffle():
    deck = Deck()
    original_order = deck.cards.copy()
    deck.shuffle()
    assert len(deck.cards) == 52
    assert deck.cards != original_order  # Ensure the order has changed

def test_deal_cards():
    deck = Deck()
    player1_hand, player2_hand = deck.deal_cards()
    assert len(player1_hand) == 26
    assert len(player2_hand) == 26
    assert set(player1_hand).isdisjoint(set(player2_hand))  # Ensure no overlap

def test_draw_card():
    deck = Deck()
    initial_length = len(deck.cards)
    card = deck.draw_card()
    assert len(deck.cards) == initial_length - 1
    assert card not in deck.cards  # Ensure the drawn card is no longer in the deck