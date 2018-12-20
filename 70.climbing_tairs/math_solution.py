# coding: utf-8
#

import math


class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        sqrt5 = math.sqrt(5)
        return int((pow((1 + sqrt5) / 2, n + 1) - pow((1 - sqrt5) / 2, n + 1))/sqrt5)
