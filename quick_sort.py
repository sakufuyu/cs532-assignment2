def quick_sort(arr, low=0, high=None):
    """
    Sorts an array in-place using the QuickSort algorithm.

    This function implements the QuickSort algorithm to sort the given array
    in ascending order. It uses the Lomuto partition scheme and is optimized
    for in-place sorting with O(log n) space complexity.

    Args:
        arr (list): The array to be sorted.
        low (int, optional): The starting index of the portion to be sorted. Defaults to 0.
        high (int, optional): The ending index of the portion to be sorted. Defaults to None.

    Returns:
        None: The function sorts the array in-place and doesn't return anything.

    Example:
        >>> numbers = [64, 34, 25, 12, 22, 11, 90]
        >>> quick_sort(numbers)
        >>> print(numbers)
        [11, 12, 22, 25, 34, 64, 90]
    """
    if (high is None):
        high = len(arr) - 1

    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    if low < high:
        pi = partition(low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


if __name__ == "__main__":
    import random
    test_array = [random.randint(1, 100) for _ in range(20)]
    print("Original array:", test_array)
    quick_sort(test_array)
    print("Sorted array:", test_array)
