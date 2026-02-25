class Character: #Parent Class
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def heal(self):
        self.health += 25
        print(f"You're Healed, Your Hp is: {self.health}")

                #Child Class
class Warrior(Character):
    def attack(self):
        print("Warrior swings sword!")

class Mage(Character):
    def attack(self):
        print("Frezze!")

class Hunter(Character):
    def attack(self):
        print("Shoot!")

class Druid(Character):
    def attack(self):
        print("Plants!")


w = Warrior("Begu", 100)
print(w.health)
m = Mage("ICE", 100)
print(m.name)
h = Hunter("Shad", 100)
print(h.name)
d = Druid("Trees", 100)
print(d.name)

w.attack()
w.heal()