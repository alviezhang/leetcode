# coding: utf-8

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        state = {}

        def dp(i, j):
            print(s, i, p, j)
            if (i, j) in state:
                return state[i, j]

            if j == len(p):
                ans = i == len(s)
            else:
                first_match = i < len(s) and p[j] in (s[i], '.')
                if j + 1 < len(p) and p[j+1] == '*':
                    ans = dp(i, j+2) or first_match and dp(i+1, j)
                else:
                    ans = first_match and dp(i+1, j+1)
                state[i, j] = ans
            return ans

        return dp(0, 0)

if __name__ == '__main__':
    assert Solution().isMatch("aa", "a") == False
    assert Solution().isMatch("aa", "aa") == True
    assert Solution().isMatch("aaa", "aa") ==  False
    assert Solution().isMatch("aa", "a*") == True
    assert Solution().isMatch("aa", ".*") == True
    assert Solution().isMatch("ab", ".*") == True
    assert Solution().isMatch("aab", "c*a*b") == True
    assert Solution().isMatch("abcd", "d*") == False
    assert Solution().isMatch("a", "ad*") == True
    assert Solution().isMatch("", "d*") == True
    assert Solution().isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c") == False
