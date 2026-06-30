from deck import Deck

def test_create_deck():
    deck = Deck()
    assert len(deck.cards) == 52
    assert all(isinstance(card, Card) for card in deck.cards)