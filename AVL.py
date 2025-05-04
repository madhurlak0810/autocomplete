# Define a node in the AVL tree
class AVLNode:
    def __init__(self, word):
        self.word = word            # The word stored at this node
        self.left = None            # Left child
        self.right = None           # Right child
        self.height = 1             # Height of the node for balancing

# Define the AVL Tree with insertion and autocomplete functionality
class AVLTree:
    # Insert a word into the AVL tree
    def insert(self, root, word):
        if not root:
            return AVLNode(word)

        if word < root.word:
            root.left = self.insert(root.left, word)
        elif word > root.word:
            root.right = self.insert(root.right, word)
        else:
            return root  # Duplicate

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        # Rebalance
        if balance > 1 and word < root.left.word:
            return self.right_rotate(root)
        if balance < -1 and word > root.right.word:
            return self.left_rotate(root)
        if balance > 1 and word > root.left.word:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and word < root.right.word:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # Height of a node
    def get_height(self, node):
        return node.height if node else 0

    # Balance factor
    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    # Left rotation
    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    # Right rotation
    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    # Main autocomplete function
    def autocomplete(self, root, prefix):
        result = []
        self._autocomplete_helper(root, prefix, result)
        return result

    # recursive helper
    def _autocomplete_helper(self, node, prefix, result):
        if not node:
            return
        if node.word.startswith(prefix):
            result.append(node.word)
            self._autocomplete_helper(node.left, prefix, result)
            self._autocomplete_helper(node.right, prefix, result)
        elif prefix < node.word:
            self._autocomplete_helper(node.left, prefix, result)
        else:
            self._autocomplete_helper(node.right, prefix, result)

# ----------- File Reading + Tree Building -----------

def build_avl_tree_from_file(filename):
    tree = AVLTree()
    root = None
    with open(filename, 'r') as f:
        for line in f:
            word = line.strip()
            if word:
                root = tree.insert(root, word)
    return tree, root

# Optional: CLI Test
if __name__ == "__main__":
    file_path = "/Users/rohanjain/Desktop/UMD - MSML/Sem 2/606/autocomplete/venv_identifiers.txt"
    tree, root = build_avl_tree_from_file(file_path)

    prefix = input("Enter prefix: ")
    matches = tree.autocomplete(root, prefix)

    print(f"\nSuggestions for prefix '{prefix}':")
    for word in matches:
        print(word)