def list_divide(numbers, divide=2):
    """
    Returns the number of elements in the numbers list that are
    divisible by divide.
    """
    count = 0
    for number in numbers:
        if number % divide == 0:
            count += 1
    return count

class ListDivideException(Exception):
    """Custom exception for list division errors."""
    pass

def test_list_divide():
    """Performs specific tests on the list_divide function."""

    # Test case 1: list_divide([1,2,3,4,5]) should return 2
    result1 = list_divide([1, 2, 3, 4, 5])
    expected1 = 2
    print(f"Test 1: {result1 == expected1}, Result: {result1}, Expected: {expected1}")

    # Test case 2: list_divide([2,4,6,8,10]) should return 5
    result2 = list_divide([2, 4, 6, 8, 10])
    expected2 = 5
    print(f"Test 2: {result2 == expected2}, Result: {result2}, Expected: {expected2}")

    # Test case 3: list_divide([30, 54, 63,98, 100], divide=10) should return 2
    result3 = list_divide([30, 54, 63, 98, 100], divide=10)
    expected3 = 2
    print(f"Test 3: {result3 == expected3}, Result: {result3}, Expected: {expected3}")

    # Test case 4: list_divide([]) should return 0
    result4 = list_divide([])
    expected4 = 0
    print(f"Test 4: {result4 == expected4}, Result: {result4}, Expected: {expected4}")

    # Test case 5: list_divide([1,2,3,4,5], 1) should return 5
    result5 = list_divide([1, 2, 3, 4, 5], 1)
    expected5 = 5
    print(f"Test 5: {result5 == expected5}, Result: {result5}, Expected: {expected5}")


if __name__ == "__main__":
    print("Running tests for list_divide:")
    test_list_divide()
