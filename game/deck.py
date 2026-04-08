from card import Card
import random

class Deck():

    def __init__(self):
        ranks = Card.accepted_ranks
        suits = Card.accepted_suits
        deck = []

        for rank in ranks:
            for suit in suits:
                print("Rank:", rank)
                print("Suit:", suit)
                print("------------")

        self.deck = deck

    def shuffle(self):
        new_deck = []
        deck = self.deck

        while True:
            if len(deck) == 1:
                card = deck[0]
                new_deck.append(card)
                break

            n = random.randint(0, len(deck)-1)

            card = deck(n)
            deck.pop(n)
            new_deck.append(card)

        print("New deck length", len(new_deck))
        print("Old deck length", len(deck))

        for card in new_deck:
            card.print_card()
            print("----")
        self.deck = new_deck
    
    def print_deck(self):
        deck = self.deck
        print("Deck size is", len(deck))
        print("------")

        for card in deck:
            card.print_card()
            print("-----------------")

    def burn_card(self):
        # take top card put it below the deck
        print("Before burning deck")
        self.print_deck()
        print("After burning")
        top_card = self.deck[0]
        self.deck.pop(0)
        self.deck.append(top_card)
        self.print_deck()

    def give_card(self):
        # take a card from the end of a deck and give out
        top_card = self.deck[0]
        self.deck.pop(0)
        return top_card

if __name__ == "__main__":
    d1=Deck()
    d1.shuffle()

    card = d1.give_card()
    print("The given card is")
    card.print_card()
    d1.print_deck()