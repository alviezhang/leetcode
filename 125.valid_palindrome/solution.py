# coding: utf-8

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # cursor
        i = -1
        j = len(s)

        # real charactor count
        left_count = 0
        right_count = 0

        s = s.lower()

        def is_valid(char):
            return 'a' <= char <= 'z' or '0' <= char <= '9'

        while True:
            while i < j:
                i += 1
                if i < min(j, len(s)) and is_valid(s[i]):
                    left_count += 1
                    break
            while j > i:
                j -= 1
                if j >= min(i, 0) and is_valid(s[j]):
                    right_count += 1
                    break

            if i >= j:
                break

            if s[i] != s[j]:
                return False

        if left_count != right_count:
            return False
        return True
