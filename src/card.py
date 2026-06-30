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
        self.suit = suit
        self.value = value

    def get_card_value(self):
        """
        Returns the numerical value of a card object.

        Returns
        -------
        int
            Integer value of a card object
        """
        return self.VALUE_TABLE[self.value]
    
    def __eq__(self, other):
        """
        Checks if two cards are equal in value but not of suit.

        Parameters
        ----------
        other : Card
            Second card object that is compaired to the object referenced on the right.

        Returns
        -------
        bool
            True if the cards have equal value.
            False if the cards do not have equal value.

        Raises
        ------
        TypeError
            If the second argument is not of type Card
        """
        if not isinstance(other, Card):
            raise TypeError("Object is not an instance of the Card class!")
        return self.value == other.value
    
    def __str__(self):
        """
        String cast function for a card object.

        Returns
        -------
        str
            String version of card data.
        """
        return f"{self.value} of {self.suit}s"