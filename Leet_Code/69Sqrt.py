'''#69 Sqrt'''
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x
        while left <= right:
            num = (left + right) // 2
            square = num * num
            if square > x:
                right = num - 1
            elif square < x:
                left = num + 1
            elif square == x:
                return num
        return left - 1
# 2
r = x
    while r*r > x:
        r = (r + x/r) / 2
    return r

# 3 this takes too much time on leetcode
class Solution(object):
    def mySqrt(self, x):
        sq = x
        while sq * sq > x:
            right = sq
            sq = sq / 2

        if sq * sq < x:
            left = sq
        elif sq * sq == x:
            sq_answer = sq
            return sq_answer

        while left < right - 1:
            sq = (left + right) / 2
            if sq * sq < x:
                left = sq
        return left