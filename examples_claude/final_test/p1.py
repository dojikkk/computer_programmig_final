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
    



"""
def deepCount(data, target):
    # base case 1: 리스트가 아니면 (= 그냥 값 하나)
    if not isinstance(data, list):
        return 1 if data == target else 0

    # base case 2: 빈 리스트면 0
    if data == []:
        return 0

    # recursive case: 첫 원소 + 나머지
    if type(data[0]) == list:
        # 첫 원소가 리스트면 → 그 안으로 들어가서 세고 + 나머지도 세기
        return deepCount(data[0], target) + deepCount(data[1:], target)
    elif data[0] == target:
        return 1 + deepCount(data[1:], target)
    else:
        return deepCount(data[1:], target)

"""