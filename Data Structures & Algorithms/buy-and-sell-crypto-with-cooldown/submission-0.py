class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Initiate dp array for three possible states, idling, cooldown, and holding
        n = len(prices)
        dp = [[0 for _ in range(n)] for _ in range(3)]

        #Set base cases (can't sell on day one, can only buy)
        dp[1][0] = float("-inf")
        dp[2][0] = -prices[0]

        #Use recurrence to populate dp array
        for i in range(1, n):
            dp[0][i] = max(dp[0][i - 1], dp[1][i - 1]) #Max between last idle and last cooldown
            dp[1][i] = dp[2][i - 1] + prices[i] #Current sale price accounting for cooldown
            dp[2][i] = max(dp[2][i - 1], dp[0][i - 1] - prices[i]) #Max between holding, our stock, or making a buy here

        return max(dp[0][-1], dp[1][-1])