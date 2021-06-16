from game_of_greed.game_logic import GameLogic , Banker

class Game:
    game_bank= Banker()
    def __init__(self, roller=None):
        self.roller = roller
        self.round = 1
        self.number_of_dice = 6
        self.Zilch = False
        # self.cheater = False
        
    def roll_dice_play(self):
        if self.number_of_dice <= 0:
            self.number_of_dice = 6
        
        print(f'Rolling {self.number_of_dice} dice...')
        dice = self.roller(self.number_of_dice)
        rolling_dice_score,rolled_dice= self.user_choice_to_tuple_and_socre(dice)
        if rolling_dice_score == 0:
            
            printable_dice = ','.join([str(d) for d in dice])
            print(printable_dice)
            print("Zilch!!! Round over")
            self.game_bank.clear_shelf()
            print(f'You banked 0 points in round {self.round}')
            self.round+=1
            self.game_bank.bank()
            print(f'Total score is {self.game_bank.balance} points')
            self.rolling()
            self.Zilch = True
            
        
        if self.Zilch == False:
            printable_dice = ','.join([str(d) for d in dice])
            print(printable_dice)
    
                
            do_quit_keep = input("Enter dice to keep (no spaces), or (q)uit: ")
            if do_quit_keep == 'q':
                self.user_quit()
            else:
                user_choice_score,user_choice_tuple = self.user_choice_to_tuple_and_socre(do_quit_keep)
                if GameLogic.cheater(dice, user_choice_tuple) == True:
                    print("Cheater!!! Or possibly made a typo...")
                    print(printable_dice)   
                    do_quit_keep = input("Enter dice to keep (no spaces), or (q)uit: ")
                    if do_quit_keep == 'q':
                        self.user_quit()
                    else:
                        user_choice_score,user_choice_tuple = self.user_choice_to_tuple_and_socre(do_quit_keep)
                        # self.cheat_and_fix(dice,user_choice_tuple)
                        self.number_of_dice = self.number_of_dice - len(user_choice_tuple)
                        self.game_bank.shelf(user_choice_score)
                        print(f'You have {self.game_bank.shelved} unbanked points and {self.number_of_dice} dice remaining')
                        # self.cheater = False
                        user_input22 = input('(r)oll again, (b)ank your points or (q)uit ')
                        self.user_choices_2(user_input22)
                else:
                        
                    self.number_of_dice = self.number_of_dice - len(user_choice_tuple)

                    self.game_bank.shelf(user_choice_score)
                    print(f'You have {self.game_bank.shelved} unbanked points and {self.number_of_dice} dice remaining')
                    # self.cheater = False
                    user_input22 = input('(r)oll again, (b)ank your points or (q)uit ')
                    self.user_choices_2(user_input22)




               

                    



    def user_choice_to_tuple_and_socre(self,user_input):
            List = list(user_input)
            int_value = [int(x) for x in List ]
            rolling_score = GameLogic.calculate_score(tuple(int_value))
            return [rolling_score,tuple(int_value)]

    def user_quit(self):
        if self.game_bank.balance != 0:
            print(f"Total score is {self.game_bank.balance} points")
        else :
            print(f"Total score is 0 points")    
        print(f'Thanks for playing. You earned {self.game_bank.balance} points')
        # exit()

    def user_choices_2(self,user_choice):
        if user_choice == 'r':
                self.roll_dice_play()
        elif user_choice =='b':
            self.number_of_dice=6
            print(f'You banked {self.game_bank.shelved} points in round {self.round}')
            self.game_bank.bank()
            print(f'Total score is {self.game_bank.balance} points')
            self.round+=1
            self.rolling()
        elif user_choice == 'q':
            self.user_quit()

    def rolling(self):
        
        # self.handle_zilch()
                
        print(f'Starting round {self.round}')
        self.number_of_dice=6
        
        self.roll_dice_play()
  
                
    def play(self):
        print("Welcome to Game of Greed")
        user_input = input("Wanna play? ")
        if user_input == 'n':
            print("OK. Maybe another time")
        else:
            self.rolling()

    
    def cheat_and_fix (self,roll_value,do_quit_keep):
        
        # keeped_value = [int(x) for x in do_quit_keep]
        if GameLogic.cheater(roll_value, do_quit_keep) == True:
            print(len(do_quit_keep))
            print(self.number_of_dice)
            self.number_of_dice = self.number_of_dice + len(do_quit_keep)
            print(self.number_of_dice)
            print("Cheater!!! Or possibly made a typo...")
            print(",".join([str(i) for i in roll_value]))
            do_quit_keep = input("Enter dice to keep (no spaces), or (q)uit: ")
            if do_quit_keep == 'q':
               self.user_quit()

            do_quit_keep = [int(x) for x in do_quit_keep]

        return do_quit_keep



    
  
                    
                    







           
             

if __name__ == "__main__":
    roller = GameLogic.roll_dice
    
    game = Game(roller)
    game.play()