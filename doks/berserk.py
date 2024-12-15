from sport.character import Character

class Berserk(Character):

    def __init__(self, name, health=100, damage=20, defense=0):
        Character.__init__(self, name, health=200, damage=50, defense=0)