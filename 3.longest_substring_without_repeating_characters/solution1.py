# coding: utf-8

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)

        if length == 0:
            return 0

        longest = 0
        start = None

        for i in range(length):
            if start is None:
                start = i
                continue

            pos = s[start:i].find(s[i])

            if pos != -1:
                if i - start > longest:
                    longest = i - start
                start = pos + start + 1

        if length - start > longest:
            longest = length - start

        return longest


if __name__ == "__main__":
    s = Solution()
    assert s.lengthOfLongestSubstring('') == 0
    assert s.lengthOfLongestSubstring('c') == 1
    assert s.lengthOfLongestSubstring('aab') == 2
    assert s.lengthOfLongestSubstring('abcabcbb') == 3
    assert s.lengthOfLongestSubstring('bbbbb') == 1
    assert s.lengthOfLongestSubstring('pwwkew') == 3
    assert s.lengthOfLongestSubstring('dvdf') == 3
