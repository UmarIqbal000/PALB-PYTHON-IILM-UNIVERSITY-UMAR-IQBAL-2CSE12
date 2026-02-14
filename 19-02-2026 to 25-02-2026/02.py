def getMinMax(arr):
    """
    Find the minimum and maximum elements in the array.

    Parameters:
        arr: List of integers

    Returns:
        List containing [minimum_element, maximum_element]
    """
    if not arr:
        return []

    min_val = arr[0]
    max_val = arr[0]

    for num in arr[1:]:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

    return [min_val, max_val]


# Test with the example
if __name__ == "__main__":
    arr = [1, 4, 3, 5, 8, 6]
    print("Input:", arr)
    result = getMinMax(arr)
    print("Output:", result)
