from typing import List
from game_of_greed.game_logic import GameLogic , Banker

class Game:

    def __init__(self, roller=None,game_bank=None):
        self.roller = roller
        self.round =1
    def play(self):
        print("Welcome to Game of Greed")
        user_input = input("Wanna play? ")
        if user_input == 'n':
            print("OK. Maybe another time")

        else:

            print(f'Starting round {self.round}')
            self.rolling()

    def rolling(self):
            print('Rolling 6 dice...')
            dice = self.roller(6)
            printable_dice = ','.join([str(d) for d in dice])
            print(printable_dice)
            do_quit_keep = input("Enter dice to keep (no spaces), or (q)uit: ")
            if do_quit_keep == 'q':
                print('Thanks for playing. You earned {game_bank.balance} points')
            # elif int(do_quit_keep) <=6 and int(do_quit_keep)>= 1:
            else:
                List=list(do_quit_keep)
                int_value=[int(x)for x in List ]
                rolling_score=GameLogic.calculate_score(tuple(int_value))
                game_bank.shelf(rolling_score)
                print(f'You have {rolling_score} unbanked points and {do_quit_keep} dice remaining')
                user_input2 =input('(r)oll again, (b)ank your points or (q)uit ')
                if user_input2 == 'a':
                    pass
                elif user_input2 =='b':
                    print(f'You banked {game_bank.shelved} points in round {self.round}')
                    game_bank.bank()
                    print(f'Total score is {game_bank.balance} points')
                    self.round+=1
                    print(f'Starting round {self.round}')
                    self.rolling()

                    
                    







           
             

if __name__ == "__main__":
    roller = GameLogic.roll_dice
    game_bank= Banker()
    game = Game(roller,game_bank)
    game.play()