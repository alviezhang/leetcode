# coding: utf-8

class Solution:
    def isMatch(self, text, pattern):
        print('isMatch: {}, {}'.format(text, pattern))
        if not pattern:
            return len(text) == 0

        first_match = text and pattern[0] in (text[0], '.')

        if len(pattern) >= 2 and pattern[1] == '*':
            return self.isMatch(text, pattern[2:]) or first_match and self.isMatch(text[1:], pattern)
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])

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
