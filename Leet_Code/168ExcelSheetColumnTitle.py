class Solution(object):
    def convertToTitle(self, number):
        """
        :type n: int
        :rtype: str
        """
        char = []
        while number > 0:
            number = number - 1
            remainder = number % 26
            char.append(chr(65 + remainder))
            number = number / 26

# 2
def convertToTitle(self, n):
    r = ''
    while (n > 0):
        n -= 1
        r = chr(n % 26 + 65) + r
        n /= 26
    return r

# 3
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        base = ord('A')
        while n:
            n, r = divmod(n - 1, 26)
            res = '{}{}'.format(chr(base + r), res)
        return res
# 4
import string

alphabet = string.ascii_uppercase

class Solution():
    def convertToTitle(self, n: int) -> str:
        result = ""

        while n > 0:
            n -= 1

            n, i = divmod(n, 26)
            result += alphabet[i]

        return result[::-1]

# 5
class Solution():
    def convertToTitle(self, num):
        alph = ''.join(map(chr, range(65, 91)))
        return (self.convertToTitle((num-1)/len(alph)) if num>len(alph) else '' )+alph[(num-1)%len(alph)]

