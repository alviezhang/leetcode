# coding: utf-8


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)

        def max_length(a, b, c):
            m = a if len(a) > len(b) else b
            return m if len(m) > len(c) else c

        def expand(i, j):
            distance = 0
            while i-distance-1>=0 and j+distance+1 < length:
                if s[i-distance-1] == s[j+distance+1]:
                    distance += 1
                else:
                    break
            return s[i-distance:j+distance+1]

        m = ''
        for i in range(length):
            r1 = expand(i, i)
            if i + 1 < length and s[i] == s[i+1]:
                r2 = expand(i, i+1)
            else:
                r2 = ''
            m = max_length(m, r1, r2)
        return m


if __name__ == '__main__':
    assert Solution().longestPalindrome('abcdefgaa') == 'aa'
    assert Solution().longestPalindrome('') == ''
    assert Solution().longestPalindrome('a') == 'a'
    assert Solution().longestPalindrome('cbbd') == 'bb'
    assert Solution().longestPalindrome('abc') in ('a', 'b', 'c')
    assert Solution().longestPalindrome('babad') in ('bab', 'aba')
    assert Solution().longestPalindrome('abcdefgaa') == 'aa'
