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
        do_quit_keep = input("Enter dice to keep (no spaces), or (q)uit: ")
        if do_quit_keep == 'q':
            self.user_quit()
        else:
            user_choice = self.user_choice_to_tuple(do_quit_keep)
            self.game_bank.shelf(user_choice)
            print(f'You have {user_choice} unbanked points and 5 dice remaining')
            user_input22 = input('(r)oll again, (b)ank your points or (q)uit ')
            self.user_choices_2(user_input22)

    def user_choice_to_tuple(self,user_input):
            List=list(user_input)
            int_value=[int(x)for x in List ]
            rolling_score=GameLogic.calculate_score(tuple(int_value))
            return rolling_score

    def user_quit(self):
        if self.game_bank.balance != 0:
            print(f"Total score is {self.game_bank.balance} points")
        print(f'Thanks for playing. You earned {self.game_bank.balance} points')

    def user_choices_2(self,user_choice):
        if user_choice == 'r':
                self.roll_dice_play()
        elif user_choice =='b':
            print(f'You banked {self.game_bank.shelved} points in round {self.round}')
            self.game_bank.bank()
            print(f'Total score is {self.game_bank.balance} points')
            self.round+=1
            self.rolling()
        elif user_choice == 'q':
            self.user_quit()

    def rolling(self):
            print(f'Starting round {self.round}')
            self.roll_dice_play()
  
                
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