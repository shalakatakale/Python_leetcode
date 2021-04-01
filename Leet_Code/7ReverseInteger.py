'''#7 Reverse Integer both input and output should be between -2**31 and 2**31-1'''
class Solution(object):
    def reverse(self, x):
        if (x.bit_length() > 31):
            return 0
        else:
            y = x
            if x < 0:
                y = -x
            output = 0
            while y:
                remainder = y % 10
                y = y // 10
                output = output * 10 + remainder

            if (output.bit_length() > 31):
                return 0
            else:
                if x < 0:
                    return -output
                else:
                    return output
# 2
class Solution(object):
    def reverse(self, x):
        if x >= -2 ** 31 and x <= 2 ** 31 - 1:
            y = x
            if x < 0:
                y = x * -1

            output = 0
            while y:
                remainder = y % 10
                y = y // 10
                output = output * 10 + remainder
            if output >= -2 ** 31 and output <= 2 ** 31 - 1:
                if x < 0:
                    return output * -1
                else:
                    return output
            else:
                return 0
        else:
            return 0

# 3
class Solution:
    def reverse(self, a: int) -> int:
        retval = int(str(abs(a))[::-1])

        if (retval.bit_length() > 31):
            return 0

        if a < 0:
            return -1 * retval
        else:
            return retval