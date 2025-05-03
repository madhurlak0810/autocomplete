import os

class RBTNode:
    def _init_(self, key, color="red"):
        self.key = key
        self.color = color  # 'red' or 'black'
        self.left = None
        self.right = None
        self.parent = None

    def is_red(self):
        return self.color == "red"

class RedBlackTree:
    def _init_(self):
        self.NIL = RBTNode(None, color="black")
        self.root = self.NIL

    def insert(self, key):
        node = RBTNode(key)
        node.left = self.NIL
        node.right = self.NIL
        node.parent = None

        parent = None
        curr = self.root
        while curr != self.NIL:
            parent = curr
            if key < curr.key:
                curr = curr.left
            else:
                curr = curr.right

        node.parent = parent
        if parent is None:
            self.root = node
        elif key < parent.key:
            parent.left = node
        else:
            parent.right = node

        node.color = "red"
        self._fix_insert(node)

    def _fix_insert(self, z):
        while z.parent and z.parent.color == "red":
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == "red":
                    z.parent.color = y.color = "black"
                    z.parent.parent.color = "red"
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self._left_rotate(z)
                    z.parent.color = "black"
                    z.parent.parent.color = "red"
                    self._right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == "red":
                    z.parent.color = y.color = "black"
                    z.parent.parent.color = "red"
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self._right_rotate(z)
                    z.parent.color = "black"
                    z.parent.parent.color = "red"
                    self._left_rotate(z.parent.parent)
        self.root.color = "black"

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def autocomplete(self, prefix):
        result = []
        self._autocomplete_helper(self.root, prefix, result)
        return result

    def _autocomplete_helper(self, node, prefix, result):
        if node == self.NIL or node.key is None:
            return
        if node.key.startswith(prefix):
            result.append(node.key)
        if prefix <= node.key:
            self._autocomplete_helper(node.left, prefix, result)
        if prefix >= node.key:
            self._autocomplete_helper(node.right, prefix, result)

def build_rbt_from_file(file_path):
    tree = RedBlackTree()
    with open(file_path, 'r') as f:
        for line in f:
            identifier = line.strip()
            if identifier:
                tree.insert(identifier)
                
    return tree