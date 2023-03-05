from random import randint


class SuperCookie:
    def __init__(self, name, superpowers):
        self.name = "supername"
        self.superpower = superpowers
        self.life_points = randint(1, 10)

    def attack(self):
        return randint(1, 10)

    def decrease_life(self, x):
        self.life_points -= x


super_cookie = SuperCookie('SuperCookie', ['sweet', 'love', 'beautifull'])
