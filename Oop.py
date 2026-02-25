import random
class Player:
    def __init__(self, name, hp = 5):
        self.name = name
        self.hp = hp

    def shoot(self, enemy):
        enemy.hp -= 1
        print(f'Shoot! -1')

    def heal(self):
        self.hp += 1
        print(f"Healed! +1 Hp is: {self.hp}")

    def alive(self, enemy):
        if enemy.hp <= 0:
            print("He's Dead")
        elif enemy.hp != 0:
            print(f"He's Alive, Opponent Hp is {enemy.hp}")


p1 = Player("Dik", 4)
p2 = Player("Koc", 4)
print("\nYou're Player 1")

while p1.hp != 0: #I think there can be any value instead p1.hp of course, if it is not equal to 0
    c = 1 #It's Limit of our Moves
    while c != 0:
        a = int(input("\nChoose Your move: \n\t'1' for Shoot\n\t'2' for Heal\n\t'3' for Check Enemy Hp\n\n\tYour Chose:"))
        print()
        if a == 1:
            p1.shoot(p2)
            c -= 1
        elif a == 2:
            p1.heal()
            c -= 1
        elif a == 3:
            p1.alive(p2)
            c -= 1
        else:
            print("You skipped your turn")
            c -= 1
    if c == 0:
        print("\n\tEnemy Move:\n")
        b = [1,2,3]
        EnemyChoice = random.choice(b)
        if EnemyChoice == 1:
            p2.shoot(p1)
            c += 1
        elif EnemyChoice == 2:
            p2.heal()
            c += 1
        elif EnemyChoice == 3:
            p2.alive(p1)
            c += 1
        else:
            print("Enemy skipped his turn")
            c += 1
    if p1.hp <= 0:
        print("Game over, You Lost!")
        break
    elif p2.hp <= 0:
        print("Game over, You Won!")
        break