import random
import time
class Player():

    def __init__(self, type="pc", cards=[], bet=0, name="", amount=0):

        self.name = name
        self.type = type
        self.cards = cards
        self._bet = bet
        self.amount = amount

    # Bet property 
    @property
    def bet(self):
        return self._bet
    
    @bet.setter
    def bet(self, amount):
        self._bet+=amount

    def place_initial_bet(self):

        while True:
            amount = input(f"Place initial bet amount. Current amount is {self.amount}: ")

            if amount.isdigit():
                n=int(amount)
                if n>0 and n<=self.amount:
                    self.amount -= n
                    return n
                
                print("Invalid amount entered.")
                print(f"Amount must range between 1 to {self.amount}")
                print("Please try again")

            else:
                print(f"Enter a number as valid amount between 1 and {self.amount}")

    def call_fold_raise(self, player):
        choice=input("Press 1 Call \n 2 Fold \n3 Raise")

        if choice=="1":
            return self.call(player)
        
        if choice=="2":
            return self.fold(player)
        
        if choice=="3":
            return self.raise_stake(player)
        
        print(f"Wrong choice {choice}. Choose 1, 2, or 3")
        self.call_fold_raise(player)


    def call(self, player):
        print("Call action")

    def fold(self, player):
        print("I fold")
        return "You lost"
    
    def raise_stake(self, player):
        print("Raise amount")

    def auto_match_or_raise(self, amount):
        print("PC thinking what to do")
        time.sleep(2)
        to_do=random.randint(1,2)
        raise_amount=amount+random.randint(10, 250)

        if raise_amount>self.amount:
            to_do=1 
            # 1 -> match

        if to_do == 1:
            if self.amount>=amount:
                self.amount-=amount
                print(f"Matching your action. Bet {amount}")
                return amount
            else:
                return "l"

        self.amount-=raise_amount
        print("I have a good feeling. I raise by ", raise_amount)
        return raise_amount

    def update_amount_bet(self, amount):
        self._bet+=amount

    def reset_amount_bet(self):
        self._bet=0 
