import pytest
from src.card import *


def test_comparison_true():
    card_a = Card("Spade", "8")
    card_b = Card("Heart", "8")
    assert (card_a == card_b) == True

def test_comparison_false():
    card_a = Card("Spade", "7")
    card_b = Card("Club", "J")
    assert (card_a == card_b) == False

def test_string_cast():
    card_a = Card("Spade", "A")
    assert str(card_a) == "Ace of Spades"
