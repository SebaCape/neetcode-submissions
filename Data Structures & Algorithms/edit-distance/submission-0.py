class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1) + 1
        m = len(word2) + 1

        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        #Set base cases
        for i in range(n):
            dp[0][i] = i
        for j in range(m):
            dp[j][0] = j

        for row in range(1, m):
            for col in range(1, n):
                val = dp[row - 1][col - 1] + (1 if word1[col - 1] != word2[row - 1] else 0)
                dp[row][col] = min(val, dp[row - 1][col] + 1, dp[row][col - 1] + 1)

        return dp[-1][-1]