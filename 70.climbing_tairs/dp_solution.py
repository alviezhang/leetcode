# coding: utf-8
#
# Define c(n) is the result of the problem, we could get:
#
#   c(n) = c(n - 1) + c(n - 2)      (n > 3)
#
#   c(1) = 1, c(2) = 2.

c = [None, 1, 2]


class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        global c
        count = len(c) - 1
        if count < n:
            c.extend([None for _ in range(n - count)])
            for i in range(count + 1, n + 1):
                c[i] = c[i-1] + c[i-2]
        return c[n]
