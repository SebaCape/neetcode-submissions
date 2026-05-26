class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        squares = []
        i = 1

        while i * i <= n:
            square = i * i
            for j in range(square, n + 1):
                dp[j] = min(dp[j - square] + 1, dp[j])
            i += 1

        return dp[n]