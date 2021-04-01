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
