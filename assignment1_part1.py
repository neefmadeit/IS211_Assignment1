def list_divide(numbers, divide=2):

    count = 0
    for number in numbers:
        if number % divide == 0:
            count += 1
    return count

class ListDivideException(Exception):
    """Custom exception for list division errors."""
    pass

def test_list_divide():

    list_divide([1, 2, 3, 4, 5])
    list_divide([2, 4, 6, 8, 10])
    list_divide([30, 54, 63, 98, 100], divide=10)
    list_divide([])
    list_divide([1, 2, 3, 4, 5], 1)

if __name__ == "__main__":
    print("Running tests for list_divide:")
    test_list_divide()
