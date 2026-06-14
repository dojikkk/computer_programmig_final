def deepSum(data):
    if data == []:
        return 0
    res = 0
    if isinstance(data[0], list):
        res += deepSum(data[0])
    else:
        res += data[0]
    res += deepSum(data[1:])
    return res

print(deepSum([1, [2, [3, [4]]], 5]))