class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]

        for row in range(m):
            for col in range(n):
                if row == 0 and col == 0:
                    continue
                elif row == 0:
                    dp[row][col] = dp[row][col - 1] + grid[row][col]
                elif col == 0:
                    dp[row][col] = dp[row - 1][col] + grid[row][col]
                else:
                    dp[row][col] = min(dp[row - 1][col], dp[row][col - 1]) + grid[row][col]

        return dp[-1][-1]
