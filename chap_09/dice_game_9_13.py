import random


class Dice:
    def __init__(self, sides=20):
        self.sides = sides

    def roll_dice(self):
        return random.randint(1, self.sides)


game = Dice()
print(game.roll_dice())
