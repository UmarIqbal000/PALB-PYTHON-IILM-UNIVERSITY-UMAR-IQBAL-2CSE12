def findUnion(a, b):
    """
    Find the union of two arrays.

    Parameters:
        a: First array of integers
        b: Second array of integers

    Returns:
        List containing all distinct elements from both arrays
    """
    # Use a set to store unique elements from both arrays
    union_set = set()

    # Add all elements from array a
    for num in a:
        union_set.add(num)

    # Add all elements from array b
    for num in b:
        union_set.add(num)

    # Convert set to list and return
    return list(union_set)


# Test with the example
if __name__ == "__main__":
    a = [1, 2, 3, 2, 1]
    b = [3, 2, 2, 3, 3, 2]
    print("Input a:", a)
    print("Input b:", b)
    result = findUnion(a, b)
    print("Output:", sorted(result))  # Sorted for consistent display
