from entities import Player
from data_loader import load_enemies, load_items
import random

# Ponto de entrada do jogo

def main():
    print("==== Bem-vindo ao AVL Adventure RPG ====")
    name = input("Digite seu nome de herói: ")
    player = Player(name)
    enemies = load_enemies()
    items = load_items()

    while True:
        print("\n1. Explorar")
        print("2. Inventário")
        print("3. Usar Item")
        print("4. Status")
        print("5. Ranking")
        print("6. Sair")
        choice = input("Escolha: ")

        if choice == "1":
            enemy_tuple = random.choice(enemies.inorder())
            enemy = enemy_tuple[1]
            print(f"\n⚔ Você encontrou um {enemy}!")

            while enemy.max_hp > 0 and player.hp > 0:
                dmg = player.attack()
                enemy.max_hp -= dmg
                print(f"Você causou {dmg} de dano. (Inimigo HP restante: {max(enemy.max_hp, 0)})")

                if enemy.max_hp > 0:
                    edmg = enemy.attack_power
                    player.hp -= edmg
                    print(f"{enemy.name} atacou! Você perdeu {edmg} de HP. (Seu HP: {max(player.hp, 0)})")

            if player.hp > 0:
                print(f"\n✅ Você derrotou o {enemy.name}! Ganhou {enemy.level * 10} XP.")
                player.add_xp(enemy.level * 10)
                if random.random() < 0.5:
                    drop = random.choice(items.inorder())
                    player.add_item(drop[0], drop[1])
                    print(f"🎁 Item encontrado: {drop[1]}")
            else:
                print("\n💀 Você foi derrotado... voltando à cidade com HP cheio.")
                player.hp = player.max_hp

        elif choice == "2":
            inv = player.inventory.inorder()
            print("\n🎒 Inventário:")
            if not inv:
                print("(vazio)")
            for k, v in inv:
                print(f"- {v}")

        elif choice == "3":
            name = input("Nome do item: ")
            result = player.use_item(name)
            print(result)

        elif choice == "4":
            print(f"\n🧙‍♂️ {player}")
            print(f"HP: {player.hp}/{player.max_hp}, ATK: {player.base_attack}")

        elif choice == "5":
            Player.global_ranking.insert(player.xp, player.name)
            print("\n🏆 Ranking de Jogadores:")
            for xp, name in reversed(Player.global_ranking.inorder()):
                print(f"- {name}: {xp} XP")

        elif choice == "6":
            print("\nAté a próxima aventura!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()

