class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #Initialize dp matrix, add extra outer layer for simplicity purposes
        m, n = len(text1), len(text2)
        dp = [[0 for _ in range (n + 1)] for _ in range (m + 1)]

        #Loop through our dp matrix to compare every possible character comparison
        for row in range(1, m + 1):
            for col in range(1, n + 1):
                #If our characters match, we want to choose the best possible subsequence length
                if text1[row - 1] == text2[col - 1]:
                    dp[row][col] = max(dp[row][col - 1], dp[row - 1][col], dp[row - 1][col - 1] + 1)
                #Note that we increment by one if both characters increased by one (sequence continuation)
                
                #The other case is that we do the same thing without incrementing, since characters differ
                else:
                    dp[row][col] = max(dp[row][col - 1], dp[row - 1][col], dp[row - 1][col - 1])

        #Get our best result
        return dp[-1][-1]