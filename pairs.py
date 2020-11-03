def find_pairs(ar, k) -> list:
    """Check how many pair combinations of elements from a given list are divisible by (the given) k

    Parameters
    ----------
    list: ar
        The given list of integers

    int: k
        The given multiple that the pairs will be checked against


    Returns
    -------
    list: pairs
        The list of tuples which are the pairs of given integers whose sum is divisible by k"""

    if not isinstance(ar, list) or not len(ar) or not k or len(ar) == 1:
        print("Error: given input is not valid")
        return list()

    for number in ar:
        if not isinstance(number, int):
            print(f"Error: {number} is not an integer")
            return list()

    pairs = list()

    for outer_loop_counter in range(0, len(ar) - 1):
        for inner_loop_counter in range(0, len(ar) - 1):
            if (ar[outer_loop_counter] + ar[inner_loop_counter]) % k == 0:
                pairs.append( (ar[outer_loop_counter], ar[inner_loop_counter]) )

    return pairs


if __name__ == "__main__":
    array = [7, 1, 3, 5, -2]
    pairs = find_pairs(array, 4)
    print(f"Original: {array}\nPairs: {pairs}")
