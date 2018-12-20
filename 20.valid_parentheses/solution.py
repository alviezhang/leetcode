# coding: utf-8

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        def get_matched(char):
            if char == ']':
                return '['
            elif char == ')':
                return '('
            elif char == '}':
                return '{'

        for i in range(len(s)):
            if s[i] in ('(', '[', '{'):
                stack.append(s[i])
            elif stack and stack[-1] == get_matched(s[i]):
                stack.pop()
            else:
                return False

        if stack:
            return False
        return True
