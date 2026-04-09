# cli final
# helps us understand our react application
# helps us with the database

from game import Game

def play_game():
    game = Game()

    human=game.human
    pc=game.pc

    game.turn=human
    #step 1 request to make bet

    human_amount=human.place_initial_bet()
    human.update_amount_bet(human_amount)

    pc_amount=pc.auto_match_or_raise(human_amount)
    pc.update_amount_bet(human_amount)

    if pc_amount=="l":
        print("Towel throwing, Human won")

    game.turn=human
    game.pot=pc_amount+human_amount

    # 1 betting round
    # 2 betting round