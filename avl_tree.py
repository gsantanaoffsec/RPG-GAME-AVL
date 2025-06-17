from __future__ import annotations
from typing import Any, Generator, Tuple, Optional

class AVLNode:
    def __init__(self, key: Any, value: Any = None):
        self.key = key
        self.value = value
        self.height = 1
        self.left: Optional[AVLNode] = None
        self.right: Optional[AVLNode] = None

    def __repr__(self):
        return f"AVLNode({self.key}:h={self.height})"

class AVLTree:
    def __init__(self):
        self.root: Optional[AVLNode] = None

    def insert(self, key: Any, value: Any = None) -> None:
        self.root = self._insert(self.root, key, value)

    def remove(self, key: Any) -> None:
        self.root = self._remove(self.root, key)

    def search(self, key: Any) -> Any | None:
        node = self._search(self.root, key)
        return node.value if node else None

    def inorder(self, reverse: bool = False) -> Generator[Tuple[Any, Any], None, None]:
        yield from self._inorder(self.root, reverse)

    def _insert(self, node: Optional[AVLNode], key: Any, value: Any) -> AVLNode:
        if node is None:
            return AVLNode(key, value)
        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:  
            node.value = value
            return node
        return self._rebalance(node)

    def _remove(self, node: Optional[AVLNode], key: Any) -> Optional[AVLNode]:
        if node is None:
            return None
        if key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:  
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            succ = self._min_node(node.right)
            node.key, node.value = succ.key, succ.value
            node.right = self._remove(node.right, succ.key)
        return self._rebalance(node)

    def _search(self, node: Optional[AVLNode], key: Any) -> Optional[AVLNode]:
        while node:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return node
        return None

    def _inorder(self, node: Optional[AVLNode], reverse: bool = False):
        if node is None:
            return
        first, second = (node.right, node.left) if reverse else (node.left, node.right)
        yield from self._inorder(first, reverse)
        yield (node.key, node.value)
        yield from self._inorder(second, reverse)

    def _rebalance(self, node: AVLNode) -> AVLNode:
        self._update_height(node)
        balance = self._balance_factor(node)
        if balance > 1:
            if self._balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1:
            if self._balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        return node

    def _rotate_left(self, z: AVLNode) -> AVLNode:
        y = z.right
        z.right = y.left
        y.left = z
        self._update_height(z)
        self._update_height(y)
        return y

    def _rotate_right(self, z: AVLNode) -> AVLNode:
        y = z.left
        z.left = y.right
        y.right = z
        self._update_height(z)
        self._update_height(y)
        return y

    def _height(self, node: Optional[AVLNode]) -> int:
        return node.height if node else 0

    def _update_height(self, node: AVLNode):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _balance_factor(self, node: AVLNode) -> int:
        return self._height(node.left) - self._height(node.right)

    def _min_node(self, node: AVLNode) -> AVLNode:
        while node.left:
            node = node.left
        return node
