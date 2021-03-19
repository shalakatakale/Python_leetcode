'''# 70 Climbing Stairs - Dynamic Programming, fibonacci numbers'''
class Solution():
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # this will take too much time on leetcode
        # ways = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        # use below
        # fibonacci
        ways, prev = 1, 0
        for i in range(1, n + 1):
            ways, prev = ways + prev, ways
        return ways
# 2
class Solution():
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <=2:
            return n
        else:
            # this will take too much time on leetcode
            # ways = self.climbStairs(n - 1) + self.climbStairs(n - 2)
            # use below
            ways, prev = 2, 1
            for i in range(3, n + 1):
                ways, prev = ways + prev, ways
        return ways


