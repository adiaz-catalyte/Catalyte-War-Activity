class Card:

    SUITS = [
        "Heart",
        "Diamond",
        "Club",
        "Spade"
    ]

    VALUE_TABLE = {
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
        "A": 14
    }

    def __init__(self, suit: str, value: str):
        
        if suit not in self.SUITS:
            raise ValueError("Your suit is not a member of accepted suit values!")
        if self.VALUE_TABLE[value] == None:
            raise ValueError("Your card value is not a member of accepted card values!")
        