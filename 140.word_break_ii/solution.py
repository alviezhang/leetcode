# coding: utf-8


class Solution:
    def wordBreak(self, s, words):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        words = set(words + [""])
        dp = [None] * (len(s) + 1)
        dp[0] = []

        for i in range(1, len(s) + 1):
            for j in range(0, i):
                if dp[j] is not None and s[j:i] in words:
                    if dp[i]:
                        dp[i].append(j)
                    else:
                        dp[i] = [j]
        if dp[-1] is None:
            return []

        paths = self._find_path(dp, [len(s)], [])
        return sorted([self._parse_path(s, path) for path in paths])

    def _parse_path(self, s, path):
        return " ".join(s[i:j] for i, j in zip(path[:-1], path[1:]))

    def _find_path(self, dp, path, result):
        for p in dp[path[-1]]:
            if p == 0:
                result.append((path + [0])[::-1])
            else:
                self._find_path(dp, path + [p], result)
        return result
