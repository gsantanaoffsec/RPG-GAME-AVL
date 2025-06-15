from avl_tree import AVLTree
import random

# Representa um item do jogo
class Item:
    def __init__(self, name: str, power: int, kind: str = "misc"):
        self.name = name
        self.power = power
        self.kind = kind

    def __str__(self):
        symbol = "+" if self.kind == "attack" else "❤" if self.kind == "heal" else "■"
        return f"{self.name} {symbol}{self.power}"

# Representa um inimigo
class Enemy:
    def __init__(self, name: str, level: int, max_hp: int, attack: int):
        self.name = name
        self.level = level
        self.max_hp = max_hp
        self.attack_power = attack

    def __str__(self):
        return f"{self.name} (Nv {self.level}, HP {self.max_hp}, ATK {self.attack_power})"

# Representa o jogador
class Player:
    global_ranking = AVLTree()  # Armazena o ranking por XP

    def __init__(self, name: str):
        self.name = name
        self.xp = 0
        self.max_hp = 100
        self.hp = 100
        self.base_attack = 10
        self.inventory = AVLTree()

    def attack(self):
        return random.randint(self.base_attack - 2, self.base_attack + 2)

    @property
    def level(self):
        return self.xp // 50 + 1

    def add_xp(self, amount):
        self.xp += amount
        self.hp = self.max_hp

    def add_item(self, name, item):
        self.inventory.insert(name, item)

    def use_item(self, name):
        item = self.inventory.search(name)
        if not item:
            return "Item não encontrado."
        if item.kind == "heal":
            healed = min(self.max_hp - self.hp, item.power)
            self.hp += healed
            result = f"Você recuperou {healed} HP." if healed else "HP já está cheio."
        elif item.kind == "attack":
            self.base_attack += item.power
            result = f"Ataque aumentado em {item.power}."
        else:
            result = "Nada aconteceu."
        self.inventory.remove(name)
        return result

    def __str__(self):
        return f"{self.name} (Nv {self.level}, XP {self.xp})"
