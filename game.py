from avl_tree import AVLTree
from entities import Player, Enemy, update_ranking, top_scores, Item
from data_loader import load_enemies, load_items
import random
import sys

WORLD_ENEMIES = AVLTree()
load_enemies(WORLD_ENEMIES)
ITEM_POOL = load_items()

MENU = """
================ AVL Adventure ================
1. Explorar
2. Inventário
3. Status
4. Ranking Global
0. Sair
==============================================="""

def choose_enemy(player: Player) -> Enemy:
    candidates = list(WORLD_ENEMIES.inorder())
    close = None
    for lvl, enemy in candidates:
        if lvl <= player.level:
            close = enemy
        elif lvl > player.level:
            close = enemy
            break
    return close.clone() if close else candidates[0][1].clone()


def explore(player: Player):
    enemy = choose_enemy(player)
    print(f"\n⚔️  Você encontrou um {enemy.name} (Lvl {enemy.level})!")
    win = enemy.fight(player)
    if win:
        print(f"\n✅ Você derrotou o {enemy.name}! XP total: {player.xp}")
        if random.random() < 0.5:
            available_items = [item for key, item in ITEM_POOL.inorder()]
            if available_items: 
                item = random.choice(available_items)
                player.add_item(item.name, item) 
                print(f"🎁 Você encontrou {item.name}!")
            else:
                print("Nenhum item disponível no pool.")
    else:
        print("\n💀 Você foi derrotado...")
        player.hp = player.max_hp  


def show_inventory(player: Player):
    print("\n📦 Inventário:")
    items = list(player.inventory.inorder())
    if not items:
        print("  (vazio)")
        return
    for i, (name, item) in enumerate(items, start=1):
        print(f"  {i}. {item.name} – {item.kind} (Power: {item.power})")
    choice = input("Usar qual item? (nome vazio = cancelar) ")
    if choice:
        print(player.use_item(choice))


def show_status(player: Player):
    print(f"\n🙍 {player.name} – Lvl {player.level}")
    print(f"HP: {player.hp}/{player.max_hp}  |  Ataque Base: {player.base_attack}  |  XP: {player.xp}")


def show_ranking():
    print("\n🏆 Ranking Global (top 10):")
    for pos, (xp, name) in enumerate(top_scores(), start=1):
        print(f" {pos:>2}. {name} – {xp} XP")


def main():
    player = Player(input("Digite seu nome: "))
    while True:
        print(MENU)
        cmd = input(">> ").strip()
        if cmd == "1":
            explore(player)
        elif cmd == "2":
            show_inventory(player)
        elif cmd == "3":
            show_status(player)
        elif cmd == "4":
            show_ranking()
        elif cmd == "0":
            break
        else:
            print("Comando inválido.")
    update_ranking(player)
    print("\nObrigado por jogar! Seu resultado foi gravado no ranking.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nSaindo...")
        sys.exit(0)
