from deck import Deck
from player import Player

class Game():

    def __init__(self):

        self.main_pot = 0

        # Deck setup
        deck = Deck()
        deck.shuffle()
        deck.shuffle()
        human_cards = [deck.give_card(), deck.give_card()]
        pc_cards = [deck.give_card(), deck.give_card()]

        self.human = Player(
            type="human",
            cards=human_cards,
            amount=0,
            name="Ronnie",
            amount=2000
        )

        self.pc = Player(
            type="pc",
            cards=pc_cards,
            amount=0,
            name="pc",
            amount=2000
        )

        self.deck = deck

    @property
    def turn(self):
        return self._turn
    
    @turn.setter
    def turn(self, player):
        
        if isinstance(player, Player):
            self._turn=player
        else:
            raise ValueError("The turn must be assigned to a player object")
        
    # Debug/ Display
    def show_hands(self):
        print("\n---Human Hand---")

        for card in self.human.cards:
            print(card)

    def show_deck(self):
        print("\n---Deck---")
        self.deck.print_deck()

if __name__ == "__main__":
    game = Game()

    '''
    game.deck.print_deck()
    print("This is the deck")
    print("PC cards")
    game.pc.cards[0].print_card()
    game.pc.cards[1].print_card()

    print("This is the deck")
    print("Human cards")
    game.human.cards[0].print_card()
    game.human.cards[1].print_card()
    '''

    game.show_deck()
    game.show_hands()

    print("\nMain pot:", game.main_pot)
