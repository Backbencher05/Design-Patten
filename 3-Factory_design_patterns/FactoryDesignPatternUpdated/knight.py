from player import Player

class Knight(Player):
    def attack(self):
        print("attack with sword")


# let in future we have new version of KnightV2

class KnightV2(Player):
    def attack(self):
        print("Attack with sword +++")