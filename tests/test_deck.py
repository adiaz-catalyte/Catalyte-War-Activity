from deck import Deck
from card import Card

def test_create_deck():
    deck = Deck()
    assert len(deck.cards) == 52
    assert all(isinstance(card, Card) for card in deck.cards)

def test_shuffle_deck():
    deck = Deck()
    original_order = deck.cards.copy()
    deck.shuffle_deck()
    assert deck.cards != original_order  # Ensure the order has changed
    assert sorted(deck.cards, key=lambda card: (card.suit, card.value)) == sorted(original_order, key=lambda card: (card.suit, card.value))  # Ensure all cards are still present

def test_deal_cards():
    deck = Deck()
    player1_cards, player2_cards = deck.deal_cards()
    assert len(player1_cards) == 26
    assert len(player2_cards) == 26
    assert all(isinstance(card, Card) for card in player1_cards)
    assert all(isinstance(card, Card) for card in player2_cards)

def test_draw_card():
    deck = Deck()
    initial_count = len(deck.cards)
    card_drawn = deck.draw_card()
    assert isinstance(card_drawn, Card)
    assert len(deck.cards) == initial_count - 1

def test_is_empty():
    deck = Deck()
    assert not deck.is_empty()
    # Draw all cards
    for _ in range(52):
        deck.draw_card()
    assert deck.is_empty()