# Classe para representar um nó da árvore AVL
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.height = 1
        self.left = None
        self.right = None

# Classe principal da árvore AVL
class AVLTree:
    def __init__(self):
        self.root = None

    # Função pública de inserção
    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)

    # Função recursiva para inserção
    def _insert(self, node, key, value):
        if not node:
            return Node(key, value)
        elif key < node.key:
            node.left = self._insert(node.left, key, value)
        else:
            node.right = self._insert(node.right, key, value)

        # Atualiza altura e reequilibra
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        return self._balance(node)

    # Busca um valor pela chave
    def search(self, key):
        node = self.root
        while node:
            if key == node.key:
                return node.value
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return None

    # Remove um nó pela chave
    def remove(self, key):
        self.root = self._remove(self.root, key)

    def _remove(self, node, key):
        if not node:
            return node
        elif key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self._get_min_value_node(node.right)
            node.key, node.value = temp.key, temp.value
            node.right = self._remove(node.right, temp.key)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        return self._balance(node)

    # Encontra o menor valor à direita
    def _get_min_value_node(self, node):
        while node.left:
            node = node.left
        return node

    def _get_height(self, node):
        return node.height if node else 0

    def _get_balance(self, node):
        return self._get_height(node.left) - self._get_height(node.right) if node else 0

    def _balance(self, node):
        balance = self._get_balance(node)
        if balance > 1:
            if self._get_balance(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1:
            if self._get_balance(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        return node

    # Rotações
    def _rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    # Retorna os dados da árvore em ordem
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append((node.key, node.value))
            self._inorder(node.right, result)
