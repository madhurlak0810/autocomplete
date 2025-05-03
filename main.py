import time
import tracemalloc
import matplotlib.pyplot as plt
from prettytable import PrettyTable

from bst import load_identifiers_into_balanced_bst
from AVL import build_avl_tree_from_file

# Global metrics storage
metrics = {
    "BST": {"time_us": 0, "memory_kb": 0, "matches": 0},
    "AVL": {"time_us": 0, "memory_kb": 0, "matches": 0},
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

    # Save metrics
    elapsed_us = (end_time - start_time) * 1e6  # microseconds
    metrics["BST"]["time_us"] = elapsed_us
    metrics["BST"]["memory_kb"] = peak / 1024
    metrics["BST"]["matches"] = len(results)

    print(f"\n[BST] Matches found: {len(results)}")
    print(f"[BST] Time taken: {elapsed_us:.2f} microseconds")
    print(f"[BST] Peak memory usage: {metrics['BST']['memory_kb']:.2f} KB")

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

    # Save metrics
    elapsed_us = (end_time - start_time) * 1e6  # microseconds
    metrics["AVL"]["time_us"] = elapsed_us
    metrics["AVL"]["memory_kb"] = peak / 1024
    metrics["AVL"]["matches"] = len(results)

    print(f"\n[AVL] Matches found: {len(results)}")
    print(f"[AVL] Time taken: {elapsed_us:.2f} microseconds")
    print(f"[AVL] Peak memory usage: {metrics['AVL']['memory_kb']:.2f} KB")

def plot_metrics():
    labels = ['BST', 'AVL']
    time_values = [metrics["BST"]["time_us"], metrics["AVL"]["time_us"]]
    memory_values = [metrics["BST"]["memory_kb"], metrics["AVL"]["memory_kb"]]

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    # Plot Time in microseconds
    axes[0].bar(labels, time_values, color=['blue', 'orange'])
    axes[0].set_title("Autocomplete Time")
    axes[0].set_ylabel("Time (microseconds)")

    # Plot Memory in KB
    axes[1].bar(labels, memory_values, color=['blue', 'orange'])
    axes[1].set_title("Peak Memory Usage")
    axes[1].set_ylabel("Memory (KB)")

    fig.suptitle("BST vs AVL Performance Comparison", fontsize=14)
    plt.tight_layout()
    plt.show()

def print_comparison_table():
    table = PrettyTable()
    table.field_names = ["Structure", "Matches Found", "Time (μs)", "Memory (KB)"]
    table.add_row([
        "BST",
        metrics["BST"]["matches"],
        f"{metrics['BST']['time_us']:.2f}",
        f"{metrics['BST']['memory_kb']:.2f}"
    ])
    table.add_row([
        "AVL",
        metrics["AVL"]["matches"],
        f"{metrics['AVL']['time_us']:.2f}",
        f"{metrics['AVL']['memory_kb']:.2f}"
    ])
    print("\n" + "="*50)
    print("Comparison Summary Table")
    print("="*50)
    print(table)

if __name__ == "__main__":
    file_path = "/Users/rohanjain/Desktop/UMD - MSML/Sem 2/606/autocomplete/venv_identifiers.txt"
    prefix = "appl"

    test_bst_autocomplete(file_path, prefix)
    test_avl_autocomplete(file_path, prefix)
    plot_metrics()
    print_comparison_table()