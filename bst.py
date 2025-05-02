import os

# --- BST Node Definition ---
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# --- BST Class with Autocomplete ---
class BST:
    def __init__(self):
        self.root = None

    def autocomplete(self, prefix):
        results = []
        self._autocomplete(self.root, prefix, results)
        return results

    def _autocomplete(self, node, prefix, results):
        if not node:
            return
        if node.value.startswith(prefix):
            results.append(node.value)
        if prefix <= node.value:
            self._autocomplete(node.left, prefix, results)
        if prefix >= node.value:
            self._autocomplete(node.right, prefix, results)

# --- Build Balanced BST from Sorted Identifiers ---
def build_balanced_bst(sorted_identifiers):
    def build_recursive(start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        node = BSTNode(sorted_identifiers[mid])
        node.left = build_recursive(start, mid - 1)
        node.right = build_recursive(mid + 1, end)
        return node

    bst = BST()
    bst.root = build_recursive(0, len(sorted_identifiers) - 1)
    return bst

# --- Load Identifiers from File and Build BST ---
def load_identifiers_into_balanced_bst(file_path):
    if not os.path.exists(file_path):
        print(f"File {file_path} not found.")
        return None

    with open(file_path, "r") as f:
        identifiers = [line.strip() for line in f if line.strip()]

    identifiers = sorted(set(identifiers))   # Ensure sorted & unique
    return build_balanced_bst(identifiers)