class Card():

    def __init__(self, suit, rank):
        
        accepted_ranks = "A","K","Q","J","10","9","8","7","6","5","4","3","2"
        accepted_suits = "HEART","DIAMOND","SPADE","CLUBS"
        
        if not isinstance(suit, str):
            raise TypeError(f"Suit expected to be a string. You got {type(suit).__name__}")
        
        if not isinstance(rank, str):
            raise TypeError(f"Rank expected to be a string.You got {type(rank).__name__}")
        
        suit_upper = suit.upper()
        rank_upper = rank.upper()

        if rank_upper in accepted_ranks:
            pass
        else:
            raise TypeError(f"Rank not in accepted ranks. Here are the accepted ranks {accepted_ranks}")
        
        if suit_upper in accepted_suits:
            pass
        else:
            raise TypeError(f"Suit not in accepted suits. Here are the accepted suits {accepted_suits}")
        

        self.rank = rank_upper
        self.suit = suit_upper

    def print_card(self):
        print("Rank", self.rank)
        print("Suit", self.suit)


if __name__ == "__main__":
    #card1 = Card(suit="Joker", rank="A")
    #card1.print_card()

    card2 = Card(suit="Clubs", rank="3")
    card2.print_card()
