class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        target = sum(nums) // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for n in nums:
            for d in range(len(dp) - 1, -1, -1):
                if dp[d] == True and n + d < len(dp):
                    dp[n + d] = True

        return dp[target]