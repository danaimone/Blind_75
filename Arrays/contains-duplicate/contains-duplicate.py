class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        non_duplicates = set(nums)
        if len(non_duplicates) != len(nums):
            return True
        else:
            return False