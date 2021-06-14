from game_of_greed.game_logic import GameLogic , Banker

class Game:
    game_bank= Banker()
    def __init__(self, roller=None):
        self.roller = roller
        self.round =1

    def roll_dice_play(self):
        print('Rolling 6 dice...')
        dice = self.roller(6)
        printable_dice = ','.join([str(d) for d in dice])
        print(printable_dice)
        return printable_dice

    def rolling(self):
            print(f'Starting round {self.round}')
            dice = self.roll_dice_play()
            do_quit_keep = input("Enter dice to keep (no spaces), or (q)uit: ")
            if do_quit_keep == 'q':
                if self.game_bank.balance != 0:
                    print(f"Total score is {self.game_bank.balance} points")
                print(f'Thanks for playing. You earned {self.game_bank.balance} points')

            else:
                List=list(do_quit_keep)
                int_value=[int(x)for x in List ]
                rolling_score=GameLogic.calculate_score(tuple(int_value))
                self.game_bank.shelf(rolling_score)
                print(f'You have {rolling_score} unbanked points and 5 dice remaining')
                user_input2 =input('(r)oll again, (b)ank your points or (q)uit ')
                if user_input2 == 'a':
                    pass
                elif user_input2 =='b':
                    print(f'You banked {self.game_bank.shelved} points in round {self.round}')
                    self.game_bank.bank()
                    print(f'Total score is {self.game_bank.balance} points')
                    self.round+=1
                    self.rolling()
                
    def play(self):
        print("Welcome to Game of Greed")
        user_input = input("Wanna play? ")
        if user_input == 'n':
            print("OK. Maybe another time")
        else:
            self.rolling()
            
  
                    
                    







           
             

if __name__ == "__main__":
    roller = GameLogic.roll_dice
    
    game = Game(roller)
    game.play()