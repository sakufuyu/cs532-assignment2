def merge_sort(arr):
    """
    Sorts an array of integers using the merge sort algorithm.

    Args:
    arr (list): An unsorted array of integers.

    Returns:
    list: A new sorted array containing the same elements as the input array.

    The function implements the merge sort algorithm, which has a time complexity of O(n log n).
    It works by recursively dividing the array into smaller subarrays, sorting them, and then
    merging the sorted subarrays back together.

    If the input array is empty or contains only one element, it is considered already sorted
    and is returned as is.

    Example:
    >>> merge_sort([6, 5, 3, 1, 8, 7, 2, 4])
    [1, 2, 3, 4, 5, 6, 7, 8]
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    """
    Merges two sorted arrays into a single sorted array.

    Args:
    left (list): A sorted array of integers.
    right (list): Another sorted array of integers.

    Returns:
    list: A new sorted array containing all elements from both input arrays.

    The function compares the first elements of the two input arrays and adds the smaller one
    to the result array. It then recursively merges the remaining elements from both arrays.

    Example:
    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    """
    result = []
    i = j = 0

    while (i < len(left) and j < len(right)):
        if (left[i] < right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


if __name__ == "__main__":
    import random
    test_array = [random.randint(1, 100) for _ in range(20)]
    print("Original array:", test_array)
    sorted_array = merge_sort(test_array)
    print("Sorted array:", sorted_array)
