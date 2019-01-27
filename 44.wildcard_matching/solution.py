class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.match(s, 0, p, 0) == 2

    def match(self, s, si, p, pi):
        """
        return value:
        0: reach the end of s but unmatched
        1: unmatched without reaching the end of s
        2: matched
        """
        if si == len(s):
            if pi == len(p):
                return 2

            elif p[pi] != '*':
                return 0

        if pi == len(p):
            return 1

        if p[pi] == '*':
            if pi + 1 < len(p) and p[pi + 1] == '*':
                return self.match(s, si, p, pi + 1)

            for t_si in range(si, len(s) + 1):
                ret = self.match(s, t_si, p, pi + 1)
                if ret == 2:
                    return ret
                # if now is unmatched and remain p, it is
                # not posible to be matched
                if ret == 0:
                    return ret

        elif p[pi] == '?' or p[pi] == s[si]:
            return self.match(s, si + 1, p, pi + 1)
        return 1


if __name__ == '__main__':
    assert Solution().isMatch('babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb', 'b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a') == False
    assert Solution().isMatch('aabababbaabbbbbaab', '******a') == False
    assert Solution().isMatch('acdcb', 'a*c?b') == False
    assert Solution().isMatch('', '**') == True
    assert Solution().isMatch('ho', 'ho**') == True
    assert Solution().isMatch('a', 'a*') == True
    assert Solution().isMatch('', '*') == True
    assert Solution().isMatch('', '?') == False
    assert Solution().isMatch('aa', 'a') == False
    assert Solution().isMatch('aa', 'aab') == False
    assert Solution().isMatch('abcdef', 'abcdef') == True
    assert Solution().isMatch('aabbccee', 'a*c*e') == True
    assert Solution().isMatch('aabbccee', '*') == True
    assert Solution().isMatch('aabbccee', '**') == True
    assert Solution().isMatch('aabbccee', '*?*') == True
    assert Solution().isMatch('aabbccee', 'a*?*e') == True
    assert Solution().isMatch('asdf', '') == False
    assert Solution().isMatch('aa', 'a?') == True
    assert Solution().isMatch('aa', 'a*') == True
