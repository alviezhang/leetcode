# coding: utf-8


class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
            n = nums[i]
            if n > 0 and n - 1 != i and n < len(nums) and nums[n - 1] != n:
                t = nums[n - 1]
                nums[n - 1] = nums[i]
                nums[i] = t
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        else:
            return len(nums) + 1
