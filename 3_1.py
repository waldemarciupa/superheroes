from random import randint

class SuperCiastko:
    def __init__(self, name, superpowers):
        self.name = "supername"
        self.superpower = superpowers
        self.life_points = randint(1,10)

    def attack(self):
        return randint(1,10)

    def decrease_life(self, x):
        self.life_points -= x

supe_ciastko = SuperCiastko('SuperCiastko', ['słodkosć', 'miłość', 'piekność'])