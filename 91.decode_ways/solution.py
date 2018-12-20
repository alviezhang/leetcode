# coding: utf-8


class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "" or s[0] == '0':
            return 0

        # Initialization
        before_previous = 0
        previous_one = 0
        current = 1

        for i in range(1, len(s)):
            before_previous = previous_one
            previous_one = current

            # When current charactor is '0', if previous charactor is in ['1', '2'],
            # f(i) = f(i-2), otherwise result is 0
            if s[i] == '0':
                if s[i-1] not in ['1', '2']:
                    return 0

                # In particular, when i = 2 or before_previous == 0, current = 1
                current = before_previous if before_previous else 1
                continue

            # f(i) = f(i - 1)
            current = previous_one

            if s[i-1] != '0' and int(s[i-1] + s[i]) <= 26:
                # f(i) = f(i - 1) + f(i - 2)
                current += before_previous if before_previous else 1

        return current
