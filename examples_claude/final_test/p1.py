def deepCount(data, target):
    """
    Recursively counts how many times 'target' appears inside 'data',
    where 'data' may be an arbitrarily nested list.

    Examples:
        deepCount([1, 2, [2, [2, 3]], 2], 2)  ->  4
        deepCount([[1], [1, [1]]], 1)         ->  3
        deepCount([], 5)                      ->  0
        deepCount(7, 7)                       ->  1
    """
    # TODO: write your recursive solution here
    if data == []:
        return 0
    elif data == [target]:
        return 1
    elif data[0] == target:
        return 1 + deepCount(data[1:], target)
    elif type(data[0]) == list:
        return deepCount(data[0], target) + deepCount(data[1:], target)
    else:
        return deepCount(data[1:], target)