def twoSum(nums: list[int], target: int) -> list[int]:
    """
    Given an array of integers nums and an integer target, return indices of two numbers
    such that they add up to target.
    :param nums:
    :param target:
    :return:
    """
    nums_dict = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in nums_dict:
            return [i, nums_dict[complement]]
        else:
            nums_dict[nums[i]] = i
    return [-1, -1]


if __name__ == "__main__":
    print(twoSum([3, 3], 6))
