# ESTAVA FALTANDO ESSE

import tkinter as tk
from tkinter import messagebox, simpledialog
from avl_tree import AVLTree
from entities import Player, Enemy, Item
from data_loader import load_enemies, load_items

class AVLAdventureGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AVL Adventure")

        self.player = None
        self.world_enemies = load_enemies()
        self.world_items = load_items()

        self.main_menu()

    def main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Bem-vindo ao AVL Adventure", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.root, text="Novo Jogo", width=30, command=self.start_new_game).pack(pady=5)
        tk.Button(self.root, text="Inventário", width=30, command=self.show_inventory).pack(pady=5)
        tk.Button(self.root, text="Explorar", width=30, command=self.explore).pack(pady=5)
        tk.Button(self.root, text="Ranking Global", width=30, command=self.show_ranking).pack(pady=5)
        tk.Button(self.root, text="Sair", width=30, command=self.root.quit).pack(pady=5)

    def start_new_game(self):
        name = simpledialog.askstring("Novo Jogo", "Digite seu nome:")
        if name:
            self.player = Player(name)
            messagebox.showinfo("Novo Jogo", f"Bem-vindo, {name}!")

    def show_inventory(self):
        if not self.player:
            messagebox.showwarning("Erro", "Inicie um jogo primeiro!")
            return
        items = self.player.inventory.in_order_traversal()
        inv_str = "\n".join([f"{k}: {v}" for k, v in items]) if items else "Inventário vazio."
        messagebox.showinfo("Inventário", inv_str)

    def show_ranking(self):
        players = Player.global_ranking.in_order_traversal()
        rank_str = "\n".join([f"{v.name}: {k}" for k, v in players]) if players else "Sem ranking ainda."
        messagebox.showinfo("Ranking Global", rank_str)

    def explore(self):
        if not self.player:
            messagebox.showwarning("Erro", "Inicie um jogo primeiro!")
            return
        enemy_node = self.world_enemies.get_closest(self.player.level)
        if not enemy_node:
            messagebox.showinfo("Explorar", "Não há inimigos disponíveis!")
            return

        enemy = enemy_node.value
        result = messagebox.askyesno("Inimigo Encontrado", f"Você encontrou {enemy.name} (Nv. {enemy.level}). Lutar?")
        if result:
            self.combat(enemy)

    def combat(self, enemy):
        if self.player.level >= enemy.level:
            messagebox.showinfo("Vitória!", f"Você derrotou {enemy.name} e subiu de nível!")
            self.player.level += 1
            self.player.score += 10
            Player.global_ranking.insert(self.player.score, self.player)
            item_node = self.world_items.get_closest(enemy.level)
            if item_node:
                self.player.add_item(item_node.key, item_node.value)
                messagebox.showinfo("Tesouro", f"Você coletou o item: {item_node.key}.")
        else:
            messagebox.showinfo("Derrota!", f"{enemy.name} era muito forte... você perdeu a batalha.")

if __name__ == '__main__':
    root = tk.Tk()
    app = AVLAdventureGUI(root)
    root.mainloop()
