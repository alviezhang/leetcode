# coding: utf-8

MAX_INT = 2147483647
MIN_INT = -2147483648


class Solution(object):
    def myAtoi(self, input_string):
        """
        :type input_string: str
        :rtype: int
        """
        number = 0
        sign = 1
        i = 0
        length = len(input_string)

        while i < length and input_string[i].isspace():
            i += 1

        if i < length and input_string[i] in ('-', '+'):
            sign = -1 if input_string[i] == '-' else 1
            i += 1

        while i < length and input_string[i].isdigit():
            number = number * 10 + ord(input_string[i]) - ord('0')

            if sign * number > MAX_INT:
                return MAX_INT
            if sign * number < MIN_INT:
                return MIN_INT

            i += 1

        return sign * number


if __name__ == '__main__':
    assert Solution().myAtoi('') == 0
    assert Solution().myAtoi(' ') == 0
    assert Solution().myAtoi(' asdfas ') == 0
    assert Solution().myAtoi(' asdfas12341') == 0
    assert Solution().myAtoi(' asdfas+12341') == 0
    assert Solution().myAtoi(' +asdfas+12341') == 0
    assert Solution().myAtoi(' -asdfas+12341') == 0
    assert Solution().myAtoi('0') == 0
    assert Solution().myAtoi('0number') == 0
    assert Solution().myAtoi('+0number') == 0
    assert Solution().myAtoi('1234') == 1234
    assert Solution().myAtoi('+1234') == 1234
    assert Solution().myAtoi('-1234asdf') == -1234
    assert Solution().myAtoi('123412341234123413241234') == MAX_INT
    assert Solution().myAtoi('-123412341234123413241234asdfasfasdfsa') == MIN_INT
