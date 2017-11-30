# coding: utf-8


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def lps(s, i, j):
            if j - i <= 1:
                return j - i
            x1, y1 = lps(i - 1, j)

        return lps(s)


if __name__ == '__main__':
    assert Solution().longestPalindrome('') == ''
    assert Solution().longestPalindrome('a') == 'a'
    assert Solution().longestPalindrome('cbbd') == 'bb'
    assert Solution().longestPalindrome('abc') in ('a', 'b', 'c')
    assert Solution().longestPalindrome('babad') in ('bab', 'aba')
