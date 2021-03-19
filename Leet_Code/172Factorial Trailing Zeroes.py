# 172. Factorial Trailing Zeroes

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        n1 = 0
        while n > 0:
            n1 += n / 5
            n = n / 5
        return n1

# 2
class Solution(object):
    def trailingZeroes(self, n):
        k, tot = 5, 0
        while k <= n:
            tot += n // k
            k = k * 5
        return tot