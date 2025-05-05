import os

# --- Optimized Trie Node ---
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

# --- Optimized Trie ---
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_end_of_word = True

    def autocomplete(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]

        return self._iterative_dfs(node, prefix)

    def _iterative_dfs(self, start_node, prefix):
        stack = [(start_node, prefix)]
        results = []

        while stack:
            node, current = stack.pop()

            if node.is_end_of_word:
                results.append(current)

            for ch in sorted(node.children.keys(), reverse=True):  # Reverse for stack LIFO order
                stack.append((node.children[ch], current + ch))

        return results

# --- Load Identifiers from File into Trie ---
def load_identifiers_into_trie(file_path):
    if not os.path.exists(file_path):
        print(f"File '{file_path}' not found.")
        return None

    trie = Trie()
    with open(file_path, "r") as f:
        for line in f:
            word = line.strip()
            if word:
                trie.insert(word)
    return trie

# --- Demo ---
if __name__ == "__main__":
    file_path = "identifiers.txt"  # Your input file
    trie = load_identifiers_into_trie(file_path)

    if trie:
        while True:
            prefix = input("\nEnter prefix (or 'exit'): ").strip()
            if prefix.lower() == "exit":
                break
            suggestions = trie.autocomplete(prefix, max_results=10)
            print(f"Suggestions for '{prefix}': {suggestions}")
