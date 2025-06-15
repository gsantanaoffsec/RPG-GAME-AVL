from avl_tree import AVLTree
from entities import Enemy, Item

# Carrega inimigos para a árvore AVL
def load_enemies():
    tree = AVLTree()
    tree.insert(1, Enemy("Goblin", 1, 30, 5))
    tree.insert(3, Enemy("Esqueleto", 3, 50, 10))
    tree.insert(5, Enemy("Orc", 5, 80, 15))
    tree.insert(8, Enemy("Mago Negro", 8, 100, 20))
    tree.insert(10, Enemy("Dragão", 10, 150, 30))
    return tree

# Carrega itens para a árvore AVL
def load_items():
    tree = AVLTree()
    tree.insert("Poção", Item("Poção", 20, "heal"))
    tree.insert("Espada", Item("Espada", 5, "attack"))
    tree.insert("Escudo", Item("Escudo", 2, "misc"))
    tree.insert("Anel Mágico", Item("Anel Mágico", 10, "attack"))
    tree.insert("Armadura", Item("Armadura", 15, "misc"))
    return tree
