from deck_of_cards import Deck


def main():
    deck = Deck()
    print(f"Initial deck size: {len(deck)} cards")
    
    deck.shuffle()
    print("Deck shuffled.")
    
    player1_hand, player2_hand = deck.deal_cards()
    print(f"Player 1 hand: {player1_hand}")
    print(f"Player 2 hand: {player2_hand}")
    
    print(f"Deck size after dealing: {len(deck)} cards")
    
    deck.reset()
    print(f"Deck reset. Current deck size: {len(deck)} cards")

if __name__ == "__main__":
    main()