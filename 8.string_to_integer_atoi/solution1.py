# coding: utf-8

MAX_INT = 2147483647
MIN_INT = -2147483648


class Solution(object):
    def myAtoi(self, input_string):
        """
        :type input_string: str
        :rtype: int
        """
        number_string = ''

        for ch in input_string:
            if ch.isdigit():
                number_string += ch
            elif not number_string and ch in ('-', '+'):
                number_string += ch
            elif number_string and ch in ('-', '+'):
                return 0
            elif not number_string and ch.isspace():
                continue
            elif not number_string:
                return 0
            elif number_string:
                break

        if not number_string or number_string in ('-', '+'):
            return 0

        number = int(number_string)
        if number > MAX_INT:
            number = MAX_INT
        if number < MIN_INT:
            number = MIN_INT

        return number


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
