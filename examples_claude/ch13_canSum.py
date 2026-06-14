def canSum(target, nums):
    if target == 0:
        return True
    elif nums == []:
        return False
    return canSum(target - nums[0], nums[1:]) or canSum(target, nums[1:])

def countSubsets(target, nums):
    if target == 0:
        return 1
    elif nums == []:
        return 0
    return countSubsets(target - nums[0], nums[1:]) + countSubsets(target, nums[1:])