from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set, longest_sequence = set(nums), 0
        for num in nums_set:
            if num - 1 in nums_set: continue
            j = 1
            while num + j in nums_set: j += 1
            longest_sequence = max(longest_sequence, j)
        return longest_sequence
