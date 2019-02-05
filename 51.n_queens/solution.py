# coding: utf-8


class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = [self.printable(queens) for queens in self.put(n, 0, [], [])]

        # for r in result:
        #     print(("\n".join(r)))
        #     print("="*n)
        return result

    def printable(self, queens):
        lines = []
        for q in queens:
            lines.append("." * q[1] + "Q" + "." * (len(queens) - q[1] - 1))
        return lines

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
