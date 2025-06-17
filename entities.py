from __future__ import annotations
import random
from avl_tree import AVLTree

class Item:
    """
    kind:
        "heal"   – recupera HP
        "attack" – aumenta ataque base
        outro     – sem efeito direto (pode usar no futuro)
    """

    def __init__(self, name: str, power: int, kind: str = "misc"):
        self.name = name
        self.power = power
        self.kind = kind

    def __str__(self):
        symbol = "+" if self.kind == "attack" else "❤" if self.kind == "heal" else "■"
        return f"{self.name} {symbol}{self.power}"

class Enemy:

    def __init__(self, name: str, level: int, max_hp: int, attack: int):
        self.name = name
        self.level = level
        self.max_hp = max_hp
        self.attack_power = attack
        self.hp = max_hp 

    def __str__(self):
        return f"{self.name} (Nv {self.level}, HP {self.max_hp}, ATK {self.attack_power})"

    def clone(self) -> Enemy:
        return Enemy(self.name, self.level, self.max_hp, self.attack_power)

    def fight(self, player: Player) -> bool:
        print(f"Iniciando combate contra {self.name}!")
        self.hp = self.max_hp 

        while player.hp > 0 and self.hp > 0:
            player_damage = player.attack()
            self.hp -= player_damage
            print(f"Você atacou {self.name} causando {player_damage} de dano. {self.name} HP: {max(0, self.hp)}/{self.max_hp}")

            if self.hp <= 0:
                player.add_xp(self.level * 10) 
                return True 

            enemy_damage = random.randint(self.attack_power - 2, self.attack_power + 2)
            player.hp -= enemy_damage
            print(f"{self.name} atacou você causando {enemy_damage} de dano. Seu HP: {max(0, player.hp)}/{player.max_hp}")

        return False 

class Player:

    global_ranking = AVLTree()

    def __init__(self, name: str):
        self.name = name
        self.xp: int = 0
        self.max_hp: int = 100
        self.hp: int = 100
        self.base_attack: int = 10
        self.inventory: AVLTree = AVLTree()

    def attack(self) -> int:
        return random.randint(self.base_attack - 2, self.base_attack + 2)

    @property
    def level(self) -> int:
        return self.xp // 50 + 1

    def add_xp(self, amount: int):
        self.xp += amount

    def add_item(self, name: str, item: Item):
        self.inventory.insert(name, item)

    def use_item(self, name: str) -> str:
        item: Item | None = self.inventory.search(name)
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

def update_ranking(player: Player) -> None:
    Player.global_ranking.insert(player.xp, player)

def top_scores(limit: int = 10) -> list[tuple[int, str]]:
    scores = []
    for xp, player in Player.global_ranking.inorder(reverse=True):
        scores.append((xp, player.name))
        if len(scores) >= limit:
            break
    return scores
