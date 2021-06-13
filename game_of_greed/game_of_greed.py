from mmap import ACCESS_READ
import random

all_rules = {
    '(1, 1)': 100,
    '(1, 2)': 200,
    '(1, 3)': 1000,
    '(1, 4)': 2000,
    '(1, 5)': 3000,
    '(1, 6)': 4000,
    '(2, 3)': 200,
    '(2, 4)': 400,
    '(2, 5)': 600,
    '(2, 6)': 800,
    '(3, 3)': 300,
    '(3, 4)': 600,
    '(3, 5)': 900,
    '(3, 6)': 1200,
    '(4, 3)': 400,
    '(4, 4)': 800,
    '(4, 5)': 1200,
    '(4, 6)': 1600,
    '(5, 1)': 50,
    '(5, 2)': 100,
    '(5, 3)': 500,
    '(5, 4)': 1000,
    '(5, 5)': 1500,
    '(5, 6)': 2000,
    '(6, 3)': 600,
    '(6, 4)': 1200,
    '(6, 5)': 1800,
    '(6, 6)': 2400,
}

class GameLogic:


        

    @staticmethod
    def roll_dice(number):
        result=[]
        for i in range (number):
            result.append(random.randint(1,6))
        return tuple(result)

    @staticmethod
    def calculate_score(roll_dice(number)):
       pass
   



class Banker:
    pass



if __name__ == "__main__":
    dice= GameLogic()
    print(dice.roll_dice(6))