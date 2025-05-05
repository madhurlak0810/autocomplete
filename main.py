import time
import tracemalloc
import matplotlib.pyplot as plt
from prettytable import PrettyTable

from bst import load_identifiers_into_balanced_bst
from AVL import build_avl_tree_from_file
from trie import load_identifiers_into_trie
from rbt import load_identifiers_into_rbt  # assuming you have this function

# Global metrics storage
metrics = {
    "BST": {"time_us": 0, "memory_kb": 0, "matches": 0},
    "AVL": {"time_us": 0, "memory_kb": 0, "matches": 0},
    "Trie": {"time_us": 0, "memory_kb": 0, "matches": 0},
    "RBT": {"time_us": 0, "memory_kb": 0, "matches": 0},
}

def test_bst_autocomplete(file_path, prefix):
    print(f"\n--- BST Autocomplete for prefix: '{prefix}' ---")
    tracemalloc.start()
    start_time = time.perf_counter()

    bst = load_identifiers_into_balanced_bst(file_path)
    results = bst.autocomplete(prefix) if bst else []

    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    for word in results:
        print(word)

    metrics["BST"]["time_us"] = (end_time - start_time) * 1e6
    metrics["BST"]["memory_kb"] = peak / 1024
    metrics["BST"]["matches"] = len(results)

def test_avl_autocomplete(file_path, prefix):
    print(f"\n--- AVL Autocomplete for prefix: '{prefix}' ---")
    tracemalloc.start()
    start_time = time.perf_counter()

    tree, root = build_avl_tree_from_file(file_path)
    results = tree.autocomplete(root, prefix)

    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    for word in results:
        print(word)

    metrics["AVL"]["time_us"] = (end_time - start_time) * 1e6
    metrics["AVL"]["memory_kb"] = peak / 1024
    metrics["AVL"]["matches"] = len(results)

def test_trie_autocomplete(file_path, prefix):
    print(f"\n--- Trie Autocomplete for prefix: '{prefix}' ---")
    tracemalloc.start()
    trie = load_identifiers_into_trie(file_path)

    start_time = time.perf_counter()
    results = trie.autocomplete(prefix) if trie else []
    end_time = time.perf_counter()

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    for word in results:
        print(word)

    metrics["Trie"]["time_us"] = (end_time - start_time) * 1e6
    metrics["Trie"]["memory_kb"] = peak / 1024
    metrics["Trie"]["matches"] = len(results)

def test_rbt_autocomplete(file_path, prefix):
    print(f"\n--- RBT Autocomplete for prefix: '{prefix}' ---")
    tracemalloc.start()
    rbt = load_identifiers_into_rbt(file_path)

    start_time = time.perf_counter()
    results = rbt.autocomplete(prefix) if rbt else []
    end_time = time.perf_counter()

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    for word in results:
        print(word)

    metrics["RBT"]["time_us"] = (end_time - start_time) * 1e6
    metrics["RBT"]["memory_kb"] = peak / 1024
    metrics["RBT"]["matches"] = len(results)

def plot_metrics():
    labels = list(metrics.keys())
    time_values = [metrics[m]["time_us"] for m in labels]
    memory_values = [metrics[m]["memory_kb"] for m in labels]

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    axes[0].bar(labels, time_values, color='skyblue')
    axes[0].set_title("Search Time (μs)")
    axes[0].set_ylabel("Time (microseconds)")

    axes[1].bar(labels, memory_values, color='lightgreen')
    axes[1].set_title("Peak Memory Usage (KB)")
    axes[1].set_ylabel("Memory (KB)")

    fig.suptitle("Autocomplete Performance Comparison", fontsize=14)
    plt.tight_layout()
    plt.show()

def print_comparison_table():
    table = PrettyTable()
    table.field_names = ["Structure", "Matches", "Search Time (μs)", "Memory (KB)"]
    for name in metrics.keys():
        table.add_row([
            name,
            metrics[name]["matches"],
            f"{metrics[name]['time_us']:.2f}",
            f"{metrics[name]['memory_kb']:.2f}"
        ])
    print("\n" + "="*60)
    print("Comparison Summary Table")
    print("="*60)
    print(table)

if __name__ == "__main__":
    file_path = "venv_identifiers.txt"
    prefix = "appl"

    test_bst_autocomplete(file_path, prefix)
    test_avl_autocomplete(file_path, prefix)
    test_trie_autocomplete(file_path, prefix)
    test_rbt_autocomplete(file_path, prefix)

    plot_metrics()
    print_comparison_table()