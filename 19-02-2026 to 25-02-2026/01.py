def reverseArray(arr):
    """
    Reverse the array in place.

    Parameters:
        arr: List of integers to be reversed

    Returns:
        The reversed array (modified in place)
    """
    left = 0
    right = len(arr) - 1

    while left < right:
        # Swap elements at left and right pointers
        arr[left], arr[right] = arr[right], arr[left]
        # Move pointers towards center
        left += 1
        right -= 1

    return arr


# Test with the example
if __name__ == "__main__":
    arr = [1, 4, 3, 2, 6, 5]
    print("Input:", arr)
    reverseArray(arr)
    print("Output:", arr)
