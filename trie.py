import os

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_end_of_word = True

    def autocomplete(self, prefix):
        results = []
        node = self.root

        # Traverse to the end of the prefix
        for ch in prefix:
            if ch not in node.children:
                return []  # No words with this prefix
            node = node.children[ch]

        self._dfs(node, prefix, results)
        return results

    def _dfs(self, node, prefix, results):
        if node.is_end_of_word:
            results.append(prefix)
        for ch, child in node.children.items():
            self._dfs(child, prefix + ch, results)

# --- Load Identifiers and Build Trie ---
def load_identifiers_into_trie(file_path):
    if not os.path.exists(file_path):
        print(f"File {file_path} not found.")
        return None

    trie = Trie()
    with open(file_path, "r") as f:
        for line in f:
            word = line.strip()
            if word:
                trie.insert(word)

    return trie
