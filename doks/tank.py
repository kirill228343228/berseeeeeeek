from sport.character import Character

class Tank(Character):

    def __init__(self, name, health=100, damage=20, defense=0):
        Character.__init__(self, name, health=150, damage=20, defense=20)


    def take_damage(self, damage):
        finale_damage = damage - self.defense if self.defense < damage else 0
        self.health = max(self.health - finale_damage, 0)
        return damage