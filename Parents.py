import random


class Entity:

    # Base for every character
    def __init__(self, name, health, damage, critChance=5, critDamage=1.5, attackMissChance=15):
        self.name = name
        self.health = health
        self.damage = damage
        self.critChance = critChance
        self.critDamage = critDamage
        self.attackMissChance = attackMissChance

    def attack(self, target):
        damage = self.damage

        if random.randint(1, 100) <= self.critChance:
            damage *= self.critDamage
            print("CRITICAL HIT!")

        target.takeDamage(damage)
    
    def heavyAttack(self, target):
        if random.randint(1, 100) <= self.attackMissChance:
            print("You missed your heavy attack!")
            return

        damage = self.damage * 1.5

        if random.randint(1, 100) <= self.critChance:
            damage *= self.critDamage
            print("CRITICAL HEAVY HIT!")

        target.takeDamage(damage)

    def takeDamage(self, damage):
        if hasattr(self, "blockPercentage"):
            originalDamage = damage
            damage *= (1 - self.blockPercentage)

            print(
                f"You blocked {self.blockPercentage * 100:.0f}% of the damage! "
                f"({originalDamage:.0f} → {damage:.0f} damage)"
            )

            self.blockPercentage = 0

        self.health = max(0, self.health - damage)

    def gainHealth(self, healthGained):
        self.health += healthGained
    
def run(self):
    if random.randint(1, 100) <= 50:
        return True
    return False



class Player(Entity):

    def __init__(self, name="You", health=100, damage=10, critChance=5, critDamage=1.5):
        super().__init__(name, health, damage, critChance, critDamage)

    def block(self):
        blockAmount = random.choice([0.75, 0.50, 0.25])
        self.blockPercentage = blockAmount


class Enemy(Entity):

    # Base class for all enemies
    pass
