from Parents import Player


class Adventurer(Player):

    # Base class with base stats
    pass


class Knight(Player):

    def __init__(self):
        # 150 HP, 25 damage, 2.5% crit chance, 1.5x crit damage
        super().__init__("You", 150, 25, 2.5)


class Mage(Player):

    def __init__(self):
        # 125 HP, 30 damage, 5% crit chance, 1.5x crit damage
        super().__init__("You", 125, 30)


class Rogue(Player):

    def __init__(self):
        # 75 HP, 15 damage, 25% crit chance, 2x crit damage
        super().__init__("You", 75, 15, 25, 2)
        
