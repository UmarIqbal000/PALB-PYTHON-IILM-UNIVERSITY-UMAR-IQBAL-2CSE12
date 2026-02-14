def kthSmallest(arr, k):
    """
    Find the kth smallest element in the given array.

    Parameters:
        arr: List of integers
        k: Integer representing which smallest element to find (1-indexed)

    Returns:
        The kth smallest element
    """
    # Sort the array in ascending order
    arr_sorted = sorted(arr)

    # Return the kth smallest (k-1 index for 0-based)
    return arr_sorted[k - 1]


# Test with the example
if __name__ == "__main__":
    arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
    k = 4
    print("Input array:", arr)
    print("k =", k)
    result = kthSmallest(arr, k)
    print("Output:", result)
