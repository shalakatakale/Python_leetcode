a = [7,5,4,3,1]
n = len(a)
dp = [[0]*3 for _ in range(n)]
print(dp)

for i in range(n):
    dp[i][0] = dp[i-1][0]
    dp[i][1] = max((dp[i-1][0] if i-1 >=0 else 0) - a[i] , dp[i-1][1] if i-1 >= 0 else -float('inf'))
    dp[i][2] = max(dp[i-1][1] + a[i] if i-1 >= 0 else -float('inf'), dp[i-1][2] if i-1 >= 0 else -float('inf'))

print(dp)


prices = [7,1,5,3,6,4]
n = len(prices)
dp = [0]*(n)
lowest_buy = prices[0]
for i in range(n):
    dp[i] = max(dp[i-1], prices[i]-lowest_buy)
    if (prices[i] <lowest_buy ):
        lowest_buy = prices[i]

print(dp)