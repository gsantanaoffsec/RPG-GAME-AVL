from avl_tree import AVLTree
from entities import Enemy, Item

def load_enemies(tree: AVLTree = None) -> AVLTree: 
    if tree is None:
        tree = AVLTree() 
    tree.insert(1, Enemy("Goblin", 1, 30, 5))
    tree.insert(3, Enemy("Esqueleto", 3, 50, 10))
    tree.insert(5, Enemy("Orc", 5, 80, 15))
    tree.insert(8, Enemy("Mago Negro", 8, 100, 20))
    tree.insert(10, Enemy("Dragão", 10, 150, 30))
    return tree

def load_items(tree: AVLTree = None) -> AVLTree:  
    if tree is None:
        tree = AVLTree()
    tree.insert("Poção", Item("Poção", 1))
    tree.insert("Espada", Item("Espada", 3))
    tree.insert("Escudo", Item("Escudo", 2))
    tree.insert("Anel Mágico", Item("Anel Mágico", 5))
    tree.insert("Armadura", Item("Armadura", 4))
    return tree
