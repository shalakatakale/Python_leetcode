'''190. Reverse Bits
Too tricky for me
Definitely not easy'''

# 1 Bit by Bit,  Time Complexity: O(1)
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ret, power = 0, 31
        while n:
            ret += (n & 1) << power
            n = n >> 1
            power -= 1
        return ret
# 2: Byte by Byte with Memoization
