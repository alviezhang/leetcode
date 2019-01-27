# coding: utf-8


class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1

        for num in range(1, max(nums) + 2):
            if num not in nums:
                return num
