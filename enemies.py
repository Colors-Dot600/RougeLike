from Parents import Enemy


class Goblin(Enemy):

    def __init__(self):
        # 50 HP, 8 damage
        super().__init__("Goblin", 50, 8)


class Skeleton(Enemy):

    def __init__(self):
        # 40 HP, 12 damage
        super().__init__("Skeleton", 40, 12)


class Zombie(Enemy):

    def __init__(self):
        # 75 HP, 10 damage
        super().__init__("Zombie", 75, 10)