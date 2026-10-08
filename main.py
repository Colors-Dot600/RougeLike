import random

from enemies import Goblin, Skeleton, Zombie
from playerCharacters import Adventurer, Knight, Mage, Rogue



# Choose your player

print("Choose your character:")
print("1. Adventurer")
print("2. Knight")
print("3. Mage")
print("4. Rogue")

choice = input("> ")

player = None

while player is None:

    print("Choose your character:")
    print("1. Adventurer")
    print("2. Knight")
    print("3. Mage")
    print("4. Rogue")

    choice = input("> ")

    if choice == "1":
        player = Adventurer()

    elif choice == "2":
        player = Knight()

    elif choice == "3":
        player = Mage()

    elif choice == "4":
        player = Rogue()

    else:
        print("Invalid choice!")


# Create enemies
goblin = Goblin()
skeleton = Skeleton()
zombie = Zombie()


# Pick a random enemy
currentEnemy = random.choice([
    goblin,
    skeleton,
    zombie
])


def battleLoop():

    print(f"{currentEnemy.name} appears!")

    print(f"{player.name}: {player.health} HP")
    print(f"{currentEnemy.name}: {currentEnemy.health} HP")

    while player.health > 0 and currentEnemy.health > 0:

        print("1. Attack")
        print("2. Heavy Attack")
        print("3. Block")

        choice = input("> ")

        # ATTACK
        if choice == "1":

            player.attack(currentEnemy)

            print(f"{currentEnemy.name}: {currentEnemy.health:.0f} HP")

            if currentEnemy.health <= 0:
                print("Enemy defeated!")
                break

            currentEnemy.attack(player)

            print(f"{player.name}: {player.health:.0f} HP")
        
        # Heavy Attack
        elif choice == "2":
            
            player.heavyAttack(currentEnemy)

            print(f"{currentEnemy.name}: {currentEnemy.health:.0f} HP")

            if currentEnemy.health <= 0:
                print("Enemy defeated!")
                break

            currentEnemy.attack(player)

            print(f"{player.name}: {player.health:.0f} HP")
            

        # BLOCK
        elif choice == "3":

            player.block()

            currentEnemy.attack(player)

            print(f"{player.name}: {player.health:.0f} HP")

        else:
            print("Invalid choice!")

    if player.health <= 0:
        print("You were defeated!")


battleLoop()