class Card():

    def __init__(self, suit, rank):
        
        accepted_ranks = "A","K","Q","J","10","9","8","7","6","5","4","3","2"
        suit_map = {
            "H": "H", "HEARTS": "H",
            "D": "D", "DIAMONDS": "D",
            "S": "S", "SPADES": "S",
            "C": "C", "CLUBS": "C"
        }
        
        if not isinstance(suit, str):
            raise TypeError(f"Suit expected to be a string. You got {type(suit).__name__}")
        
        if not isinstance(rank, str):
            raise TypeError(f"Rank expected to be a string.You got {type(rank).__name__}")
        
        suit_upper = suit.upper()
        rank_upper = rank.upper()

        # Suit handling
        if suit_upper in suit_map:
            self.suit = suit_map[suit_upper]
        else:
            raise ValueError("Invalid suit. Use H/D/S/C or full names.")

        # Handle ranks
        if rank_upper not in accepted_ranks:
            raise ValueError(f"Rank not in accepted ranks. Here are the accepted ranks {accepted_ranks}")
        
        self.rank = rank_upper
    
    def __repr__(self):
        return f"{self.rank}{self.suit}"

    def print_card(self):
        print("Rank", self.rank)
        print("Suit", self.suit)



#if __name__ == "__main__":
    #card1 = Card(suit="Joker", rank="A")
    #card1.print_card()

    #card2 = Card(suit="Clubs", rank="3")
    #card2.print_card()
