'''# 70 Climbing Stairs - Dynamic Programming, fibonacci numbers'''
# 1 Brute force climbStairs(i,n)=climbStairs(i+1,n)+climbStairs(i+2,n)
# where ii defines the current step and nn defines the destination step.
# Time O(n**2) # space O(n)
# Run time exceeds on leetcode
class Solution():
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.climb_Stairs(0, n)

    def climb_Stairs(self, i, n):
        if i > n:
            return 0
        if i == n:
            return 1

        return self.climb_Stairs(i + 1, n) + self.climb_Stairs(i + 2, n)

# best complexity O(log(n)) by Binets Method
# too much math see leetcode
# And also fibonacci formula gives O(log(n))

# Recursion with memoization
# Time O(n)
# Space O(n)
class Solution():
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = [0] * n
        return self.climb_Stairs(0, n, memo)

    def climb_Stairs(self, i, n, memo):
        if i > n:
            return 0
        if i == n:
            return 1
        if memo[i] > 0:
            return memo[i]

        memo[i] = self.climb_Stairs(i + 1, n, memo) + self.climb_Stairs(i + 2, n, memo)
        print(memo)
        return memo[i]

n = 5
answer = Solution()
answer.climbStairs(n)

# DP time O(n)
# space O(n) because we have array
class Solution():
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 2)
        # [0,1,1,2,3,5,8] : dp[0] and dp[1] are assigned by us
        # so we need length of dp to be n+2
        dp[1] = 1
        for i in range(2, n + 2):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n + 1]


#Finonacci
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


