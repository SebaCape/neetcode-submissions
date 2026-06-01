class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        n_nums = [1] + nums + [1] #For simplicity of operations

        #DP matrix for mximum coins collectable from bursting within some range left to right in our new nums array
        dp = [[0 for _ in range(n + 2)] for _ in range(n + 2)]

        #Start from last balloons we can burst
        for l in range(n, 0, -1):
            #Check every possible bound within this range
            for r in range(l, n + 1):
                #Check all burst indices within that range and save our maximum
                for i in range(l, r + 1):
                    coins = n_nums[l - 1] * n_nums[i] * n_nums[r + 1]
                    coins += dp[l][i - 1] + dp[i + 1][r]
                    dp[l][r] = max(dp[l][r], coins)

        #Aggregated maximum value is stored at this dp index
        return dp[1][n]