def largest(arr):
    """
    Find the largest element in the given array.

    Parameters:
        arr: List of integers

    Returns:
        The largest element in the array
    """
    # Initialize max_val with first element
    max_val = arr[0]

    # Iterate through array to find maximum
    for num in arr[1:]:
        if num > max_val:
            max_val = num

    return max_val


# Test with the example
if __name__ == "__main__":
    arr = [1, 8, 7, 56, 90]
    print("Input:", arr)
    result = largest(arr)
    print("Output:", result)
