import random

class GameLogic:


   @staticmethod
   def calculate_score():
       pass







   @staticmethod
   def roll_dice(number):
        result=[]
        for i in range (number):
           result.append(random.randint(1,6))
        return  tuple(result)









class Banker:
    pass



if __name__ == "__main__":
    dice= GameLogic()
    print(dice.roll_dice(6))