from sport.character import Character


class Berserk(Character):

    damage_multiplier = 1.5
    rage_limit = 50


    def __init__(self, name, health=100, damage=20, defense=0,
        damage_multiplier= 1.5, rage_limit=50):
        Character.__init__(self, name, health=150, damage=40, defense=0)
        self.damage_multiplier = damage_multiplier
        self.rage_limit = rage_limit


    def attack(self, target):
        final_damage = self.damage * self.damage_multiplier \
            if self.health < self.rage_limit else self.damage
        return target.take_damage(final_damage)