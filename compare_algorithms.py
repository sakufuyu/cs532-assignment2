import time
import random
import copy
import math
from merge_sort import merge_sort
from quick_sort import quick_sort


def performance_comparison(arr_sizes):
    """
    Function to compare performance of merge sort and quick sort

    Parameters:
        arr_sizes: List of array sizes to test
    """
    results = []

    for size in arr_sizes:
        # Generate various datasets
        sorted_array = list(range(size))
        random_array = list(range(size))
        random.shuffle(random_array)
        reverse_sorted = list(range(size, 0, -1))

        # Measure execution time for both algorithms on each dataset
        datasets = {
            "sorted": sorted_array,
            "random": random_array,
            "reverse_sorted": reverse_sorted
        }

        size_results = {"size": size}

        for name, dataset in datasets.items():
            # Measure merge sort time
            start_time = time.time()
            merge_sort(copy.deepcopy(dataset))
            merge_time = time.time() - start_time

            # Measure quick sort (in-place) time
            quick_array = copy.deepcopy(dataset)
            start_time = time.time()
            quick_sort(quick_array)
            quick_time = time.time() - start_time

            size_results[f"{name}_merge_sort"] = merge_time
            size_results[f"{name}_quick_sort"] = quick_time

        results.append(size_results)
        print(f"Processing for size {size} completed")

    return results


# Test execution
if __name__ == "__main__":
    arr_sizes = [10, 50, 100, 200, 300, 500]
    results = performance_comparison(arr_sizes)

    # Display results
    print("\n==== Performance Comparison Results ====")
    for result in results:
        n = result['size']
        theoretical_value = n * math.log2(n) if n > 0 else 0
        # Normalize theoretical value to match execution time scale
        normalized_theoretical = theoretical_value * 1e-7  # Adjust scale to match actual execution time
        print(f"\nData size: {n}")
        print(f"{'Theoretical O(n log n)':<25}: {normalized_theoretical:.6f} seconds")
        for key, value in result.items():
            if key != "size":
                print(f"{key:<25}: {value:.6f} seconds")
