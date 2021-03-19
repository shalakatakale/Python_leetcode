'''#122 Best time to sell stock
you can make as many transactions as you want to make maximum profit'''
class Solution(object):
    def maxProfit(self, prices):
        # profit3 = [0]*len(prices)
        profit = []
        for i in range(len(prices) - 1):
            if prices[i] >= prices[i + 1]:
                None
            else:
                profit.append(prices[i + 1] - prices[i])
                # profit = prices[i+1]-prices[i]
        profit = sum(profit)
        return profit


