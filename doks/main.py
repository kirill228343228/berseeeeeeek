from sport.character import Character
from berserk import Berserk

player1 = Character("Andrei", 240, 20, 0)
player1.print_stats()

player2 = Berserk("Roma", 200, 30, 0)
player2.print_stats()

player3 = Character("Katia")
player3.print_stats()

player1.attack(player2)

print("\n\n")
player1.print_stats()
player2.print_stats()
