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

    # Pre-flop Betting
    print("\n---Pre-Flop---")

    human_amount=human.place_initial_bet()
    human.update_amount_bet(human_amount)

    pc_amount=pc.auto_match_or_raise(human_amount)
    pc.update_amount_bet(human_amount)

    if pc_amount=="l":
        print("Throwing in the towel, Human wins")
        return
    
    pc.update_amount_bet(pc_amount)

    game.turn=human
    game.pot+=pc_amount+human_amount
    print("Pot:", game.main_pot)

    '''
    k = 0

    # 1 betting round
    print("--------------------------")
    print("Starting the first betting round")
    print("--------------------------")
    while True:
        #human and PC -> call, raise, fold
        if k>1 and pc.amount == human.amount:
            return "Betting round one completed"
        
        k=k+1
        
        amount=human.call_fold_raise(player=pc)
    # 2 betting round

    '''
    # Flop
    print("\n---Flop---")
    flop = [game.deck.give_card() for _ in range(3)]
    print("Flop:", flop)
    
    result = betting_round(game)

    if result:
        return
    
    # Turn
    print("\n---Turn---")
    turn_card = game.deck.give_card()
    print("Turn:", turn_card)

    result = betting_round(game)
    if result:
        return
    
    # River
    print("\n---River---")
    river_card = game.deck.give_card()
    print("River:", river_card)

    result = betting_round(game)
    if result:
        return
    
    # Showdown
    print("\n---SHowdown---")
    print("HUman:", human.cards)
    print("PC:", pc.cards)
    print("Board included, no evaluation yet.")
    
    
    print("Winner TBD")

def betting_round(game):
    human = game.human
    pc = game.pc

    print("\n---Betting Round---")

    while True:
        
        # End conditio
        if human.bet == pc.bet:
            print("Betting round complete")
            break

        # Human action
        action = human.call_fold_raise()

        if action == "fold":
            print("Human folded. PC wins")
            return "pc"
        
        if action == "raise":
            amount = human.place_initial_bet(amount)
            
            human.update_amount_bet(amount)

            game.mainpot+=amount


    # pC response
    pc_amount = pc.auto_match_or_raise(human.bet)

    if pc_amount == "l":
        print("PC folded. Human wins")
        return "human"
    
    pc.update_amount_bet(pc_amount)
    game.main_pot+=pc.amount

    print("Current pot:", game.main_pot)

    return None


if __name__=="__main__":
    play_game()