'''121 Best time to buy and sell stocks'''
# see dp.py file too

## below is python greedy
class Solution(object):
    def maxProfit(self,prices):
        buy, profit = float('inf'), 0
        for price in prices:
            buy, profit = min(buy, price), max(profit, price-buy)
        return profit

## Dp O(n**2)
class Solution(object):
    def maxProfit(self, a):
        if not a: return 0
        n = len(a)
        # dp[i][state] where state = 0: doing nothing, 1: buy, 2: sell
        dp = [[0]*3 for _ in range(n)]
        for i in range(n):
            # dp[i][0] = dp[i-1][0]
            dp[i][1] = max( -a[i] , dp[i-1][1] if i-1 >= 0 else -float('inf'))
            dp[i][2] = max(dp[i-1][1] + a[i] if i-1 >= 0 else -float('inf'), dp[i-1][2] if i-1 >= 0 else -float('inf'))
        return  max(dp[n-1][0], dp[n-1][2])

# DP O(n)
class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0

        n = len(prices)
        dp = [0] * (n)
        lowest_buy = prices[0]
        for i in range(n):
            dp[i] = max(dp[i - 1], prices[i] - lowest_buy)
            if (prices[i] < lowest_buy):
                lowest_buy = prices[i]

        return dp[n - 1]

#
class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
            maxProfit = 0
            minPurchase = prices[0]
            for i in range(1, len(prices)):
                maxProfit = max(maxProfit, prices[i] - minPurchase)
                minPurchase = min(minPurchase, prices[i])
                return maxProfit

# I wrote below fails for [3,2,6,5,0,3]
# Output:
# 3
# Expected:
# 4
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        while prices:
            buy = min(prices)
            buy_index = prices.index(buy)
            if buy_index == len(prices) - 1:
                prices.pop(-1)
            else:
                new_prices = prices[buy_index + 1:]
                sell = max(new_prices)
                profit = sell - buy
                if profit <= 0:
                    return 0
                else:
                    return profit
        return 0

# fails for  Input:
# [7,6,4,3,1]
# Output:
# 5
# Expected:
# 0
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sort_prices = sorted(prices)
        left = 0
        right = len(sort_prices) -1
        while left < right:
            if prices.index(sort_prices[left]) > prices.index(sort_prices[right]):
                left +=1
                profit_1 = sort_prices[right] - sort_prices[left]
                left -=1
                right -= 1
                profit_2 = sort_prices[right] - sort_prices[left]
            return max(profit_1, profit_2)