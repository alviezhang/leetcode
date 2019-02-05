# coding: utf-8


class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        return len(self.put(n, 0, [], []))

    def check(self, queens, pos):
        for i, j in queens:
            if i == pos[0]:
                return False
            if j == pos[1]:
                return False
            if i + j == pos[0] + pos[1]:
                return False
            if i - j == pos[0] - pos[1]:
                return False
        return True

    def put(self, n, level, queens, result):
        if level == n:
            result.append(queens)
            return

        for i in range(n):
            if self.check(queens, (level, i)):
                self.put(n, level+1, queens + [(level, i)], result)
        return result
